from sentence_transformers import SentenceTransformer

model = None

def generate_embedding(text: str):

    global model

    if model is None:
        model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    embedding = model.encode(text)

    return embedding.tolist()