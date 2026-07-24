from fastapi import APIRouter
from app.services.analytics_service import AnalyticsService

router = APIRouter(
    prefix="/analytics",
    tags=["AI Analytics"]
)

@router.get("/usage")
def usage():
    return AnalyticsService.ai_usage()