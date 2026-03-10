import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    system_instruction=(
        "You are a helpful and knowledgeable assistant. "
        "Answer questions clearly, accurately, and concisely. "
        "If you don't know the answer, say so honestly."
    )
)

def answer_question(question: str) -> str:
    response = model.generate_content(question)
    return response.text
