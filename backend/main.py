from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.auth import router as auth_router
from app.api.users import router as users_router
from app.api.dashboard import router as dashboard_router
from app.api.report import router as report_router
from app.api.notifications import router as notification_router
from app.api.upload import router as upload_router
from app.api.chat import router as chat_router
from app.api.knowledge_base import router as kb_router
from app.api.analytics_ai import router as analytics_router
from app.api.delete_document import router as delete_router
from app.api.memory import router as memory_router

app = FastAPI(title="Business Backend API")

app.include_router(health_router)
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(dashboard_router)
app.include_router(report_router)
app.include_router(notification_router)
app.include_router(upload_router)
app.include_router(chat_router)
app.include_router(kb_router)
app.include_router(analytics_router)
app.include_router(delete_router)
app.include_router(memory_router)

@app.get("/")
def root():
    return {
        "service": "Business Backend",
        "status": "running"
    }