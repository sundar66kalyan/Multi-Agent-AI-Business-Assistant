from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.auth import router as auth_router
from app.api.users import router as users_router
from app.api.chat import router as chat_router
from app.api.upload import router as upload_router
from app.api.knowledge_base import router as knowledge_router
from app.api.delete_document import router as delete_router
from app.api.report import router as report_router
from app.api.dashboard import router as dashboard_router
from app.api.notifications import router as notification_router

from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.include_router(health_router)
#app.include_router(auth_router)
#app.include_router(users_router)
#app.include_router(chat_router)
#app.include_router(upload_router)
#app.include_router(knowledge_router)
#app.include_router(delete_router)
#app.include_router(report_router)
#app.include_router(dashboard_router)
#app.include_router(notification_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to Multi-Agent AI Business Assistant"
    }