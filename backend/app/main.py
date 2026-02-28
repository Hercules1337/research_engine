# backend/app/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict
from utils import call_ollama_model
from config import WORKER_MODELS, JUDGE_MODEL, WORKER_TEMP, JUDGE_TEMP
from prompts import WORKER_PROMPT_TEMPLATE, JUDGE_PROMPT_TEMPLATE

app = FastAPI(title="Local LLM Research Engine")

class QueryRequest(BaseModel):
    query: str

class JudgeResponse(BaseModel):
    summary: str
    similarities: str
    discrepancies: str

@app.post("/query", response_model=JudgeResponse)
def query_ai(request: QueryRequest):
    query = request.query
    worker_outputs = []

    # Step 1: Run worker models sequentially
    for model in WORKER_MODELS:
        prompt = WORKER_PROMPT_TEMPLATE.format(query=query)
        output = call_ollama_model(model, prompt)
        worker_outputs.append(f"{model}: {output}")

    # Step 2: Run judge model on all worker outputs
    judge_prompt = JUDGE_PROMPT_TEMPLATE.format(worker_outputs="\n".join(worker_outputs))
    judge_output = call_ollama_model(JUDGE_MODEL, judge_prompt)

    # For simplicity, return judge_output as all fields (later you can parse JSON)
    return {
        "summary": judge_output,
        "similarities": "See judge output",
        "discrepancies": "See judge output"
    }

@app.get("/")
def root():
    return {"message": "LLM Research Engine running"}
