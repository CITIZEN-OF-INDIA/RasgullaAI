import os
import uuid

from rag.embeddings import generate_embedding
from rag.chroma_db import add_document


# Backend folder path
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# backend/data
DATA_FOLDER = os.path.join(
    BASE_DIR,
    "data"
)


def chunk_text(text):
    """
    Split text into chunks of roughly 1500 characters.
    """

    chunks = []

    current_chunk = ""

    lines = text.split("\n")

    for line in lines:

        if len(current_chunk) + len(line) < 500:
            current_chunk += line + "\n"

        else:
            chunks.append(current_chunk.strip())
            current_chunk = line + "\n"

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks


def index_file(file_path):

    filename = os.path.basename(file_path)

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as f:

        content = f.read()

    chunks = chunk_text(content)

    print(
        f"Processing {filename} "
        f"({len(chunks)} chunks)"
    )

    for chunk in chunks:

        embedding = generate_embedding(chunk)

        add_document(
            doc_id=str(uuid.uuid4()),
            text=chunk,
            embedding=embedding,
            metadata={
                "source": filename
            }
        )

    print(f"Indexed {filename}")


def main():

    print(f"Using data folder: {DATA_FOLDER}")

    if not os.path.exists(DATA_FOLDER):
        raise FileNotFoundError(
            f"Data folder not found: {DATA_FOLDER}"
        )

    for file in os.listdir(DATA_FOLDER):

        if file.endswith(".txt"):

            index_file(
                os.path.join(
                    DATA_FOLDER,
                    file
                )
            )

    print("\nIndexing completed successfully.")


if __name__ == "__main__":
    main()