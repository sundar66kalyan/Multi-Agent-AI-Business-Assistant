from fastapi import FastAPI

from app.api.chat import router as chat_router
from app.api.upload import router as upload_router
from app.api.stats import router as stats_router

app = FastAPI(
    title="AI Service",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "service": "AI Service",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


app.include_router(chat_router)
app.include_router(upload_router)
app.include_router(stats_router)