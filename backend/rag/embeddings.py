from functools import lru_cache

from chromadb.utils import embedding_functions


@lru_cache(maxsize=1)
def _get_embedding_function():
    return embedding_functions.DefaultEmbeddingFunction()


def generate_embedding(text: str):
    if not text or not text.strip():
        raise ValueError("Cannot generate an embedding for empty text.")

    embedding_function = _get_embedding_function()
    embeddings = embedding_function([text])

    return embeddings[0]
