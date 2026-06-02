from rag.chroma_db import search_documents


def retrieve_context(question: str, top_k: int = 5):
    """
    PURE CHROMA SEARCH VERSION
    (NO TORCH, NO SENTENCE-TRANSFORMERS)
    """

    # Chroma will handle embedding internally IF collection was built with embeddings
    results = search_documents(
        query_embedding=question,  # raw text now
        n_results=top_k
    )

    documents = results.get("documents", [[]])[0]

    if not documents:
        return ""

    return "\n\n".join(documents)