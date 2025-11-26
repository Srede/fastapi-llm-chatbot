from pydantic import BaseModel
from typing import List, Optional


class ChatRequest(BaseModel):
    message: str


class SimilarQuestion(BaseModel):
    id: int
    question: str
    domain: str
    subdomain: str
    complexity: str


class ChatResponse(BaseModel):
    original_question: str
    is_valid: bool
    refined_question: Optional[str] = None
    similar_questions: List[SimilarQuestion] = []
