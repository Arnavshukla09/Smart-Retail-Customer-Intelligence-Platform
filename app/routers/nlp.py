from fastapi import APIRouter
from schemas import TextRequest, SentimentResponse
from services.nlp_service import nlp_service

router = APIRouter()

@router.post("/analyze-sentiment", response_model=SentimentResponse)
async def analyze_sentiment(req: TextRequest):
    return nlp_service.analyze_sentiment(req.text)
