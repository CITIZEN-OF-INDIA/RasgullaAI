from rag.embeddings import generate_embedding
from rag.chroma_db import search_documents


def retrieve_context(question: str, top_k: int = 5):

    query_embedding = generate_embedding(question)

    results = search_documents(
        query_embedding=query_embedding,
        n_results=top_k
    )

    documents = results.get("documents", [[]])[0]

    if not documents:
        return ""

    return "\n\n".join(documents)