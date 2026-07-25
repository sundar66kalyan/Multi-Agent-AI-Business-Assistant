from fastapi import APIRouter

from app.rag.vectordb import VectorDB

router = APIRouter(
    prefix="/stats",
    tags=["Statistics"]
)


@router.get("/")
def stats():

    db = VectorDB()

    return {
        "indexed_chunks": db.count()
    }