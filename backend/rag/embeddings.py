from sentence_transformers import SentenceTransformer
import threading

# Load once globally (safe + predictable)
_model = None
_lock = threading.Lock()

MODEL_NAME = "all-MiniLM-L6-v2"


def _load_model():
    global _model
    if _model is None:
        with _lock:
            if _model is None:  # double-check locking
                _model = SentenceTransformer(
                    MODEL_NAME,
                    device="cpu"  # important for Render memory stability
                )
    return _model


def generate_embedding(text: str):
    """
    Returns embedding as a Python list.
    Safe for concurrent API requests.
    """
    model = _load_model()
    embedding = model.encode(text, convert_to_numpy=True)
    return embedding.tolist()