from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard/stats")
async def get_stats():
    return {
        "daily_visits": 150,
        "returning_customers": 45,
        "sentiment_score": 8.5,
        "top_category": "electronics"
    }
