import json
import os
import numpy as np
from modules.storage import storage
from sentence_transformers import SentenceTransformer

# default storage.json 
_DEFAULT_STORAGE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "storage.json")

# Embed each exemplar's `label` and persist items + embeddings to storage.json.
def build_storage(items: list, output_path: str = _DEFAULT_STORAGE_PATH) -> list:
    encoder = SentenceTransformer("all-mpnet-base-v2")
    labels  = [item["label"] for item in items]   # the text we embed for retrieval
    vectors = encoder.encode(labels, normalize_embeddings=True, show_progress_bar=True)

    # attach the embedding back onto each item so it travels with the json
    for item, vec in zip(items, vectors):
        item["embedding"] = vec.tolist()

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

    print(f"Saved {len(items)} examples to {output_path}")
    return items


# Load the exemplar bank from disk, returning (items, embeddings matrix).
def load_storage(path: str = _DEFAULT_STORAGE_PATH):
    items      = json.load(open(path, encoding="utf-8"))
    # Stack the per-item embeddings into one (n_items x dim) matrix.
    embeddings = np.array([item["embedding"] for item in items])
    return items, embeddings


_encoder_cache: SentenceTransformer | None = None

# Return the encoder, loading it once and caching it.
def _get_encoder() -> SentenceTransformer:
    global _encoder_cache
    if _encoder_cache is None:
        _encoder_cache = SentenceTransformer("all-mpnet-base-v2")
    return _encoder_cache

# Retrieve the top-k most similar items from the exemplar bank.
def retrieve(question: str, items: list, embeddings: np.ndarray, k: int = 5) -> list:
    enc    = _get_encoder()
    q_vec  = enc.encode([question], normalize_embeddings=True)
    scores = np.dot(embeddings, q_vec.T).flatten()   # cosine sim to every exemplar
    top_k  = np.argsort(scores)[::-1][:k]            # indices of the k highest scores
    # Map those indices back to their exemplar dicts, most similar first.
    return [items[i] for i in top_k]

# build storage.json from modules.storage.
if __name__ == "__main__":
    build_storage(storage, _DEFAULT_STORAGE_PATH)
