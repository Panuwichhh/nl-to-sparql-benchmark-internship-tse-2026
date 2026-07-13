"""
Usage:
    python run_flow2_execution.py \
        --input path/to/source.jsonl \
        --output path/to/results.jsonl \
        --endpoint http://localhost:8083/sparql
"""

import argparse
import json
import sys
import time
from pathlib import Path

import requests


RUN_FIELDS = [
    ("run1", "sparql_run1", "cosine_sim_run1"),
    ("run2", "sparql_run2", "cosine_sim_run2"),
    ("run3", "sparql_run3", "cosine_sim_run3"),
]

QUERY_TIMEOUT = 30    # per-query timeout in seconds

def pick_best_run(row: dict):
    best = None
    for label, sparql_key, cos_key in RUN_FIELDS:
        sparql_text = row.get(sparql_key)
        cos_val = row.get(cos_key)
        if not sparql_text or not isinstance(sparql_text, str) or not sparql_text.strip():
            continue
        if cos_val is None:
            continue
        if best is None or cos_val > best[2]:
            best = (label, sparql_text, cos_val)
    return best if best else (None, None, None)


def run_sparql_query(endpoint: str, query: str, timeout: int):
    result = {
        "success": False,
        "http_status": None,
        "error": None,
        "columns": [],
        "row_count": 0,
        "rows": [],
    }

    headers = {"Accept": "application/sparql-results+json"}
    params = {"query": query}

    try:
        resp = requests.get(endpoint, params=params, headers=headers, timeout=timeout)
    except requests.exceptions.RequestException as e:
        result["error"] = f"request_exception: {e}"
        return result

    result["http_status"] = resp.status_code

    if resp.status_code != 200:
        result["error"] = f"http_{resp.status_code}: {resp.text[:500]}"
        return result

    try:
        data = resp.json()
    except ValueError as e:
        result["error"] = f"json_decode_error: {e} | body: {resp.text[:500]}"
        return result

    try:
        columns = data.get("head", {}).get("vars", [])
        bindings = data.get("results", {}).get("bindings", [])
    except AttributeError as e:
        result["error"] = f"unexpected_response_shape: {e}"
        return result

    rows = []
    for b in bindings:
        row_dict = {var: b[var].get("value") for var in b}
        rows.append(row_dict)

    result["success"] = True
    result["columns"] = columns
    result["row_count"] = len(bindings)
    result["rows"] = rows
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--input", required=True, help="Path to source eval jsonl file")
    ap.add_argument("--output", required=True, help="Path to write new jsonl results")
    ap.add_argument("--endpoint", default="http://localhost:8083/sparql", help="Ontop SPARQL endpoint URL")
    args = ap.parse_args()

    in_path = Path(args.input)
    out_path = Path(args.output)

    total = 0
    ok = 0
    failed = 0
    skipped = 0

    t0 = time.time()

    def print_progress(done: int, ok_: int, failed_: int, skipped_: int, elapsed: float, end=""):
        msg = (
            f"\r[{done}] processed"
            f"  ok={ok_} failed={failed_} skipped={skipped_}"
            f"  {elapsed:.1f}s"
        )
        sys.stderr.write(msg + end)
        sys.stderr.flush()

    with in_path.open("r", encoding="utf-8") as fin, out_path.open("w", encoding="utf-8") as fout:
        for line in fin:
            line = line.strip()
            if not line:
                continue

            row = json.loads(line)
            total += 1

            run_label, sparql_text, cosine_sim = pick_best_run(row)

            if sparql_text is None:
                skipped += 1
                out_record = {
                    "model": row.get("model"),
                    "id": row.get("id"),
                    "question": row.get("question"),
                    "prompt_style": row.get("prompt_style"),
                    "chosen_run": None,
                    "cosine_sim": None,
                    "sparql": None,
                    "endpoint": args.endpoint,
                    "success": False,
                    "http_status": None,
                    "error": "no_valid_run_found",
                    "columns": [],
                    "row_count": 0,
                    "rows": [],
                }
                fout.write(json.dumps(out_record, ensure_ascii=False) + "\n")
                elapsed = time.time() - t0
                print_progress(total, ok, failed, skipped, elapsed)
                continue

            exec_result = run_sparql_query(args.endpoint, sparql_text, QUERY_TIMEOUT)

            if exec_result["success"]:
                ok += 1
            else:
                failed += 1

            out_record = {
                "model": row.get("model"),
                "id": row.get("id"),
                "question": row.get("question"),
                "prompt_style": row.get("prompt_style"),
                "chosen_run": run_label,
                "cosine_sim": cosine_sim,
                "sparql": sparql_text,
                "endpoint": args.endpoint,
                **exec_result,
            }
            fout.write(json.dumps(out_record, ensure_ascii=False) + "\n")
            fout.flush()

            elapsed = time.time() - t0
            print_progress(total, ok, failed, skipped, elapsed)

    elapsed = time.time() - t0
    if total == 0:
        print(f"No rows found in {in_path}.", file=sys.stderr)
        return
    # Finish the inline progress line, then print summary
    print_progress(total, ok, failed, skipped, elapsed, end="\n")
    print("=" * 50, file=sys.stderr)
    print(f"Done. total={total} ok={ok} failed={failed} skipped={skipped} | {elapsed:.1f}s elapsed", file=sys.stderr)
    print(f"Output written to: {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()