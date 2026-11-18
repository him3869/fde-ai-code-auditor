import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

app = FastAPI(title="FDE Code Review Agent")
client = genai.Client()

class CodeRequest(BaseModel):
    code: str
    language: str = "python"

class CodeReviewResponse(BaseModel):
    is_safe: bool
    bugs_found: list[str]
    optimization_suggestions: list[str]
    refactored_code: str

def load_system_prompt() -> str:
    try:
        with open("prompt-1.txt", "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "You are a helpful code review assistant."

@app.get("/")
def serve_frontend():
    return FileResponse("index.html")

@app.post("/review-code", response_model=CodeReviewResponse)
def review_code(request: CodeRequest):
    system_prompt = load_system_prompt()
    user_content = f"Language: {request.language}\n\nCode to review:\n{request.code}"

    try:
        response = client.models.generate_content(
            model='gemini-3.8-flash',
            contents=user_content,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                response_mime_type="application/json",
                response_schema=CodeReviewResponse,
                temperature=0.2,
            ),
        )
        return response.parsed
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
