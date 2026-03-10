import os
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from agent import answer_question

app = FastAPI(title="QA Agent")

@app.get("/")
def health_check():
    return {"status": "ok", "agent": "qa-agent"}

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
        answer = answer_question(question)
        return JSONResponse({"answer": answer})
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
```

---

## `requirements.txt`
```
google-generativeai
fastapi
uvicorn[standard]
