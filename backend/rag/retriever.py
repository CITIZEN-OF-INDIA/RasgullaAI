import re
from functools import lru_cache
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"


def _tokenize(text: str):
    return re.findall(r"[a-z0-9+#.]+", text.lower())


def _chunk_text(text: str, max_words: int = 140):
    words = text.split()

    if not words:
        return []

    return [
        " ".join(words[start:start + max_words])
        for start in range(0, len(words), max_words)
    ]


@lru_cache(maxsize=1)
def _load_chunks():
    chunks = []

    if not DATA_DIR.exists():
        return chunks

    for file_path in sorted(DATA_DIR.glob("*.txt")):
        text = file_path.read_text(encoding="utf-8").strip()

        for chunk in _chunk_text(text):
            chunks.append(
                {
                    "source": file_path.name,
                    "text": chunk,
                    "tokens": set(_tokenize(chunk)),
                }
            )

    return chunks


def retrieve_context(question: str, top_k: int = 5):
    query_tokens = set(_tokenize(question))

    if not query_tokens:
        return ""

    scored_chunks = []

    for chunk in _load_chunks():
        overlap = query_tokens.intersection(chunk["tokens"])

        if not overlap:
            continue

        source_tokens = set(_tokenize(chunk["source"]))
        source_boost = len(query_tokens.intersection(source_tokens))
        score = len(overlap) + (source_boost * 2)

        scored_chunks.append((score, chunk))

    scored_chunks.sort(key=lambda item: item[0], reverse=True)

    selected_chunks = [
        f"Source: {chunk['source']}\n{chunk['text']}"
        for _, chunk in scored_chunks[:top_k]
    ]

    return "\n\n".join(selected_chunks)
