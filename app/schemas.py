from pydantic import BaseModel
from typing import Optional

class TextRequest(BaseModel):
    text: str

class ChatRequest(BaseModel):
    message: str

class SentimentResponse(BaseModel):
    status: str
    sentiment: str
    confidence: float

class ChatResponse(BaseModel):
    reply: str
    error: Optional[str] = None

class FaceRecognitionResponse(BaseModel):
    face_detected: bool
    customer_id: Optional[str] = None
    name: Optional[str] = None
    loyalty_tier: Optional[str] = None
    status: str
    visit_count: Optional[int] = None
    match_confidence: Optional[float] = None

class ProductClassificationResponse(BaseModel):
    status: str
    category: str
    confidence: float
