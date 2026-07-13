import os
import re
import time
import json
import urllib.request
import urllib.error
from datetime import datetime

from dotenv import load_dotenv
load_dotenv()  

import numpy as np
from sentence_transformers import SentenceTransformer
from openai import OpenAI

from modules.utils.questions import get_questions
QUESTIONS = get_questions()
from modules.utils.prompting_utils import build_prompt, PROMPT_STYLES
from modules.dfsl import load_storage, retrieve
from modules.utils.eval_utils import extract_sparql


# CONFIG
API_TIMEOUT      = 600   
RUNS             = 3     # LLM calls per question+style 
SLEEP_SEC        = 1.0   # request delay 
COSINE_THRESHOLD = 0.9   # mean cosine >= this will PASS
EMBED_MODEL_NAME = "jinaai/jina-embeddings-v2-base-code"

_ollama_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")

_openai_client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    timeout=120,
)

_ollama_client = OpenAI(
    base_url=_ollama_url,
    api_key="ollama",
    timeout=API_TIMEOUT,
)

BACKENDS = [
    {
        "label":    "openai/" + os.getenv("OPENAI_MODEL", "gpt-4o"),
        "provider": "openai",
        "client":   _openai_client,
        "model":    os.getenv("OPENAI_MODEL", "gpt-4o"),
        "timeout":  API_TIMEOUT,
    },
    {
        "label":    "ollama/deepseek-coder:6.7b",
        "provider": "ollama",
        "client":   _ollama_client,
        "model":    "deepseek-coder:6.7b",
        "base_url": _ollama_url,
        "timeout":  API_TIMEOUT,
        "num_ctx":  8192,
    },
    {
        "label":    "ollama/qwen2.5-coder:7b",
        "provider": "ollama",
        "client":   _ollama_client,
        "model":    "qwen2.5-coder:7b",
        "base_url": _ollama_url,
        "timeout":  API_TIMEOUT,
        "num_ctx":  8192,
    },
    {
        "label":    "ollama/codegemma:instruct",
        "provider": "ollama",
        "client":   _ollama_client,
        "model":    "codegemma:instruct",
        "base_url": _ollama_url,
        "timeout":  API_TIMEOUT,
        "num_ctx":  8192,
    },
    {
        "label":    "ollama/llama3.1:8b",
        "provider": "ollama",
        "client":   _ollama_client,
        "model":    "llama3.1:8b",
        "base_url": _ollama_url,
        "timeout":  API_TIMEOUT,
        "num_ctx":  8192,
    },
]

_TS          = datetime.now().strftime("%Y%m%d_%H%M%S")
OUTPUT_JSONL = f"results/eval/sparql_eval_results_{_TS}.jsonl"


# OLLAMA HEALTH CHECK
def check_ollama(model: str, base_url: str) -> bool:
    host = base_url.replace("/v1", "")
    try:
        with urllib.request.urlopen(f"{host}/api/tags", timeout=5) as r:
            data = json.loads(r.read())
        available = [m["name"] for m in data.get("models", [])]
    except urllib.error.URLError as e:
        print(f"[Ollama] [ERROR]  Server not responding at {host}  ({e.reason})")
        return False
    except Exception as e:
        print(f"[Ollama] [WARN]  Could not read model list: {e}")
        return True 
    if model not in available:
        print(f"[Ollama] [ERROR]  Model '{model}' not in backend")
        print(f"         Available: {available}")
        print(f"         Run 'ollama pull {model}' first")
        return False

    print(f"[Ollama] [OK]  model='{model}' ready")
    return True

# SCORING
def cosine_sim(vec_a: np.ndarray, vec_b: np.ndarray) -> float:
    denom = np.linalg.norm(vec_a) * np.linalg.norm(vec_b)
    return float(np.dot(vec_a, vec_b) / denom) if denom else 0.0

#compute mean cosine similarity between label and predictions
def compute_scores(embed_model: SentenceTransformer, label: str, predictions: list[str]) -> dict:
    vecs = embed_model.encode([label] + predictions, convert_to_numpy=True)
    sims = [cosine_sim(vecs[0], vecs[i + 1]) for i in range(len(predictions))]
    mean = float(np.mean(sims))
    return {
        "sims":    sims,
        "mean":    round(mean, 4),
        "std":     round(float(np.std(sims)), 4),
        "verdict": "PASS" if mean >= COSINE_THRESHOLD else "FAIL",
    }


# LLM CALL
def call_llm(backend: dict, messages: list[dict], retries: int = 3) -> str:
    extra_body = {"options": {"num_ctx": backend["num_ctx"]}} if backend.get("num_ctx") else {}
    for attempt in range(1, retries + 1):
        try:
            resp = backend["client"].chat.completions.create(
                model       = backend["model"],
                messages    = messages,
                temperature = 0.0,
                timeout     = backend.get("timeout", API_TIMEOUT),
                extra_body  = extra_body,
            )
            return resp.choices[0].message.content.strip()
        except KeyboardInterrupt:
            raise
        except Exception as e:
            if attempt == retries:
                return f"ERROR: {e}"
            wait = 2 ** attempt
            print(f"      [retry {attempt}/{retries}] {type(e).__name__} — waiting {wait}s...")
            time.sleep(wait)
    return "ERROR: max retries exceeded"



# JSONL EXPORT
def export_jsonl(rows: list[dict], path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp_path = path + ".part"
    with open(tmp_path, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    os.replace(tmp_path, path)

# checkpoint - save progress
def checkpoint_jsonl(rows: list[dict], path: str, tag: str = "") -> None:
    if not rows:
        return
    try:
        export_jsonl(rows, path)
        print(f"     [checkpoint] saved {len(rows)} rows -> {path}  {tag}")
    except Exception as e:
        print(f"     [checkpoint] WARN  save skipped ({type(e).__name__}: {e})  {tag}")



# EVALUATION LOOP
def _build_row(
    backend: dict,
    q: dict,
    style: str,
    results: list[str],
    latencies: list[float],
    scores: dict | None,
) -> dict:
    row: dict = {
        "model":        backend["label"],
        "id":           q["id"],
        "question":     q["question"],
        "prompt_style": style,
        "sparql_label": q.get("sparql_label", ""),
        "cosine_mean":  scores["mean"]    if scores else "",
        "cosine_std":   scores["std"]     if scores else "",
        "verdict":      scores["verdict"] if scores else "",
        "latency_mean": round(float(np.mean(latencies)), 3),
    }
    for i, (r, lat) in enumerate(zip(results, latencies), 1):
        row[f"R{i}"]              = r                       # raw model output (CoT keeps reasoning)
        row[f"sparql_run{i}"]     = extract_sparql(r) or ""  # cleaned query — re-runnable later
        row[f"latency_run{i}"]    = round(lat, 3)
        row[f"cosine_sim_run{i}"] = scores["sims"][i - 1] if scores else ""
    return row

def run_evaluation():
    for backend in BACKENDS:
        if backend["provider"] == "ollama":
            if not check_ollama(backend["model"], backend.get("base_url", _ollama_url)):
                return

    print("Loading embedding model...")
    embed_model = SentenceTransformer(EMBED_MODEL_NAME, trust_remote_code=True)
    print("Embedding model ready.\n")

    retrievers: dict[str, object] = {}
    # for DFSL prompt style - load storage
    if any(s.startswith("DFSL") for s in PROMPT_STYLES):
        _dfsl_items, _dfsl_emb = load_storage()
        if "DFSL" in PROMPT_STYLES:
            retrievers["DFSL"] = lambda q: retrieve(q, _dfsl_items, _dfsl_emb, k=5)
            print(f"DFSL storage loaded: {len(_dfsl_items)} examples")
        print()

    rows      = []
    total     = len(BACKENDS) * len(PROMPT_STYLES) * len(QUESTIONS) * RUNS
    done      = 0
    run_start = time.perf_counter()

    print(f"{'='*60}")
    print(f"NL to PARQL Evaluation  |  backends={len(BACKENDS)}  |  runs={RUNS}")
    print(f"Models: {[b['label'] for b in BACKENDS]}")
    print(f"Styles: {len(PROMPT_STYLES)}  |  Questions: {len(QUESTIONS)}  |  Total calls: {total}")
    print(f"{'='*60}\n")

    for backend in BACKENDS:
        print(f"{'─'*60}\n>>  Backend: {backend['label']}\n{'─'*60}")
        backend_start = time.perf_counter()

        for style in PROMPT_STYLES:
            print(f"  Prompt Style: {style}")

            for q in QUESTIONS:
                results, latencies = [], []
                for run in range(1, RUNS + 1):
                    messages = build_prompt(style, q["question"], retriever=retrievers.get(style))
                    t0       = time.perf_counter()
                    sparql   = call_llm(backend, messages)
                    elapsed  = time.perf_counter() - t0
                    results.append(sparql)
                    latencies.append(elapsed)
                    done += 1
                    print(f"     Q{q['id']:02d} Run{run} [{done}/{total}] done  ({elapsed:.2f}s)")
                    time.sleep(SLEEP_SEC)

                label  = q.get("sparql_label", "")
                pred_queries = [extract_sparql(r) or "" for r in results]
                scores = compute_scores(embed_model, label, pred_queries) if label.strip() else None
                rows.append(_build_row(backend, q, style, results, latencies, scores))

            checkpoint_jsonl(rows, OUTPUT_JSONL, tag=f"[{backend['label']} | {style}]")
            print()

        elapsed = time.perf_counter() - backend_start
        print(f"  [time]  Backend '{backend['label']}' total: {elapsed:.1f}s ({elapsed/60:.1f} min)\n")

    export_jsonl(rows, OUTPUT_JSONL)
    print(f"{'='*60}\n  Done!  jsonl → {OUTPUT_JSONL}\n{'='*60}")


if __name__ == "__main__":
    run_evaluation()
