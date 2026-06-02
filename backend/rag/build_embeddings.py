import os
import chromadb
from sentence_transformers import SentenceTransformer

# ----------------------------
# Paths
# ----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
CHROMA_DIR = os.path.join(BASE_DIR, "chroma_storage")

# ----------------------------
# Load embedding model (ONLY LOCAL USAGE)
# ----------------------------
model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")

# ----------------------------
# Chroma DB setup
# ----------------------------
client = chromadb.PersistentClient(path=CHROMA_DIR)

collection = client.get_or_create_collection(
    name="rasgulla_ai_knowledge"
)

# ----------------------------
# Simple text chunker
# ----------------------------
def chunk_text(text, chunk_size=300, overlap=50):
    words = text.split()
    chunks = []

    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks


# ----------------------------
# Load all .txt files
# ----------------------------
def load_documents():
    docs = []

    for file_name in os.listdir(DATA_DIR):
        if file_name.endswith(".txt"):
            file_path = os.path.join(DATA_DIR, file_name)

            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()

                chunks = chunk_text(text)

                for i, chunk in enumerate(chunks):
                    doc_id = f"{file_name}_{i}"

                    docs.append((doc_id, chunk, file_name))

    return docs


# ----------------------------
# Build embeddings + store in Chroma
# ----------------------------
def build_vector_db():
    docs = load_documents()

    texts = []
    ids = []
    embeddings = []
    metadatas = []

    print(f"Processing {len(docs)} chunks...")

    for doc_id, text, source in docs:
        embedding = model.encode(text, convert_to_numpy=True)

        ids.append(doc_id)
        texts.append(text)
        embeddings.append(embedding.tolist())
        metadatas.append({"source": source})

    collection.add(
        ids=ids,
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas
    )

    print("Vector DB built successfully!")


# ----------------------------
# Run script
# ----------------------------
if __name__ == "__main__":
    build_vector_db()