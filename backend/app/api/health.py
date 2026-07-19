from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():

    return {
        "status": "Healthy",
        "application": "Multi-Agent AI Business Assistant",
        "version": "1.0.0"
    }