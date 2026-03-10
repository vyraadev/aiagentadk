import os
import google.generativeai as genai

api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable is not set")

genai.configure(api_key=api_key)
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    system_instruction=(
        "You are a helpful and knowledgeable assistant. "
        "Answer questions clearly, accurately, and concisely. "
        "If you don't know the answer, say so honestly."
    )
)

def answer_question(question: str) -> str:
    try:
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        raise Exception(f"Gemini API error: {str(e)}")
