from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.auth import router as auth_router
from app.api.users import router as users_router
from app.api.dashboard import router as dashboard_router

app = FastAPI()

app.include_router(health_router)
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(dashboard_router)

@app.get("/")
def root():
    return {"status": "OK"}