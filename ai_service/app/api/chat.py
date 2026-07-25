from fastapi import APIRouter
from app.services.chat_service import ChatService

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@router.post("/")
def ask(payload: dict):

    print("=" * 60)
    print("CHAT ENDPOINT CALLED")
    print("Payload:", payload)
    print("=" * 60)

    question = payload.get("question", "")

    chat = ChatService()

    return chat.ask(question)