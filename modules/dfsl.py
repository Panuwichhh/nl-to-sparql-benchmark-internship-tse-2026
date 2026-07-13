import json
import os
import numpy as np
from modules.storage import storage
from sentence_transformers import SentenceTransformer

# default storage.json 
_DEFAULT_STORAGE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "storage.json")

# build vector storage
def build_storage(items: list, output_path: str = _DEFAULT_STORAGE_PATH) -> list:
    encoder = SentenceTransformer("all-mpnet-base-v2")
    labels  = [item["label"] for item in items]
    vectors = encoder.encode(labels, normalize_embeddings=True, show_progress_bar=True)

    for item, vec in zip(items, vectors):
        item["embedding"] = vec.tolist()

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

    print(f"Saved {len(items)} examples to {output_path}")
    return items

# load vector storage
def load_storage(path: str = _DEFAULT_STORAGE_PATH):
    items      = json.load(open(path, encoding="utf-8"))
    embeddings = np.array([item["embedding"] for item in items])
    return items, embeddings


_encoder_cache: SentenceTransformer | None = None

# get encoder
def _get_encoder() -> SentenceTransformer:
    global _encoder_cache
    if _encoder_cache is None:
        _encoder_cache = SentenceTransformer("all-mpnet-base-v2")
    return _encoder_cache

# retrieve top k examples
def retrieve(question: str, items: list, embeddings: np.ndarray, k: int = 5) -> list:
    enc    = _get_encoder()
    q_vec  = enc.encode([question], normalize_embeddings=True)
    scores = np.dot(embeddings, q_vec.T).flatten()
    top_k  = np.argsort(scores)[::-1][:k]
    return [items[i] for i in top_k]

# build vector storage from storage
if __name__ == "__main__":
    build_storage(storage, _DEFAULT_STORAGE_PATH)
