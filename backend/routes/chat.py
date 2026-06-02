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
    try:
        context = retrieve_context(request.question)

        prompt = build_prompt(
            question=request.question,
            context=context
        )

        answer = ask_gemini(prompt)

        return {"answer": answer}

    except Exception as e:
        print("🔥 ERROR IN CHAT FLOW:", e)

        return {
        "answer": "Backend error occurred",
        "error": str(e)
    }