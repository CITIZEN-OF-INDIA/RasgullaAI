import os
import chromadb


# Backend directory
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# backend/chroma_storage
CHROMA_PATH = os.path.join(
    BASE_DIR,
    "chroma_storage"
)

# Create persistent client
client = chromadb.PersistentClient(
    path=CHROMA_PATH
)

# Collection
collection = client.get_or_create_collection(
    name="rasgulla_ai_knowledge",
    embedding_function=None  # we will set proper strategy during build step
)


def add_document(
    doc_id,
    text,
    embedding,
    metadata=None
):
    """
    Add document chunk to ChromaDB.
    """

    collection.add(
        ids=[doc_id],
        documents=[text],
        embeddings=[embedding],
        metadatas=[metadata or {}]
    )


def search_documents(
    query_embedding,
    n_results=3
):
    """
    Search similar documents.
    """

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results