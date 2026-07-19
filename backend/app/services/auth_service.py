from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.services.auth import hash_password, verify_password
from app.core.security import create_access_token


class AuthService:

    @staticmethod
    def register(db: Session, full_name: str, email: str, password: str):

        existing = UserRepository.get_by_email(db, email)

        if existing:
            raise HTTPException(
                status_code=400,
                detail="Email already registered."
            )

        user = User(
            full_name=full_name,
            username=email,
            email=email,
            hashed_password=hash_password(password),
            role="Administrator"
        )

        return UserRepository.create(db, user)

    @staticmethod
    def login(db: Session, email: str, password: str):

        user = UserRepository.get_by_email(db, email)

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password."
            )

        if not verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password."
            )

        token = create_access_token(
            {
                "sub": user.email,
                "role": user.role
            }
        )

        return {
            "access_token": token,
            "user": {
                "name": user.full_name,
                "email": user.email,
                "role": user.role
            }
        }