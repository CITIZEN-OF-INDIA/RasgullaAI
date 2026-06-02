import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(
    api_key=GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def ask_gemini(prompt: str) -> str:
    """
    Sends prompt to Gemini and returns response text.
    """

    try:
        response = model.generate_content(prompt)

        if hasattr(response, "text"):
            return response.text.strip()

        return "An error occured. Lemme fix it in a while!"

    except Exception as e:
        print(f"Gemini Error: {e}")

        return f"Gemini Error: {str(e)}"