from fastapi import APIRouter

from app.memory.memory_store import memory

router = APIRouter(
    prefix="/history",
    tags=["History"]
)


@router.get("/")
def get_history():

    return {
        "success": True,
        "history": memory.messages
    }


@router.delete("/")
def clear_history():

    memory.clear()

    return {
        "success": True
    }