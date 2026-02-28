# backend/app/models.py

from pydantic import BaseModel
from typing import List, Dict

# Request from user
class QueryRequest(BaseModel):
    query: str

# Response from judge
class JudgeResponse(BaseModel):
    summary: str
    similarities: str
    discrepancies: str
