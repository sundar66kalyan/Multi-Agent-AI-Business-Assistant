from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.user import UserCreate, UserLogin
from app.services.auth_service import AuthService

router = APIRouter(tags=["Authentication"])


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    new_user = AuthService.register(
        db,
        user.full_name,
        user.email,
        user.password
    )

    return {
        "message": "User registered successfully.",
        "user_id": new_user.id
    }


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    result = AuthService.login(
        db,
        user.email,
        user.password
    )

    return {
        "access_token": result["access_token"],
        "token_type": "bearer",
        "user": result["user"]
    }