from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.orchestrator.orchestrator_service import Orchestrator
from app.schemas.chat import ChatRequest
from app.memory.memory_store import memory

router = APIRouter(tags=["Chat"])


@router.post("/chat")
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db)
):
    orchestrator = Orchestrator()

    import inspect

    print("=" * 60)
    print(inspect.getfile(orchestrator.__class__))
    print("=" * 60)

    memory.add(
        role="user",
        content=request.message
    )

    result = orchestrator.process(
        message=request.message,
        db=db
    )

    memory.add(
        role="assistant",
        content=str(result)
    )

    return result