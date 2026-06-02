from fastapi import APIRouter
from pydantic import BaseModel

from rag.retriever import retrieve_context
from rag.prompt_builder import build_prompt

from services.gemini_service import ask_gemini

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
def chat(request: ChatRequest):

    # Step 1: Retrieve relevant chunks from ChromaDB
    context = retrieve_context(
        request.question
    )

    # Step 2: Build RAG prompt
    prompt = build_prompt(
        question=request.question,
        context=context
    )

    # Step 3: Send to Gemini
    answer = ask_gemini(prompt)

    return {
        "answer": answer
    }