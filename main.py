import os
import uuid
import uvicorn
import asyncio
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part
from agent import root_agent

app = FastAPI(title="QA Agent")

session_service = InMemorySessionService()
runner = Runner(
    agent=root_agent,
    session_service=session_service,
    app_name="qa_agent",
)

@app.get("/")
def health_check():
    return {"status": "ok", "agent": "qa_agent"}

@app.post("/ask")
async def ask(request: Request):
    try:
        body = await request.json()
        question = body.get("question", "").strip()
        if not question:
            return JSONResponse(
                status_code=400,
                content={"error": "'question' field is required"}
            )

        session_id = str(uuid.uuid4())
        user_message = Content(
            role="user",
            parts=[Part(text=question)]
        )

        response_text = ""
        async for event in runner.run_async(
            user_id="user",
            session_id=session_id,
            new_message=user_message,
        ):
            if event.is_final_response() and event.content:
                response_text = event.content.parts[0].text
                break

        return JSONResponse({"answer": response_text})

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)

