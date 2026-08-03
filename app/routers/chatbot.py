from fastapi import APIRouter
from schemas import ChatRequest, ChatResponse
from services.chatbot_service import chatbot_service

router = APIRouter()

@router.post("/chatbot", response_model=ChatResponse)
async def chat(req: ChatRequest):
    return chatbot_service.get_reply(req.message)
