from fastapi import APIRouter
from app.memory.memory_store import memory

router = APIRouter(tags=["Memory"])


@router.get("/memory")
def get_memory():
    return {
        "total_messages": len(memory.get_history()),
        "history": memory.get_history()
    }


@router.delete("/memory")
def clear_memory():
    memory.clear()

    return {
        "success": True,
        "message": "Conversation memory cleared."
    }