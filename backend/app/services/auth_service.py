from fastapi import HTTPException
from sqlalchemy.orm import Session
import traceback

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
        try:
            print("LOGIN STEP 1")

            user = UserRepository.get_by_email(db, email)
            print("LOGIN STEP 2", user)

            if not user:
                raise HTTPException(
                    status_code=401,
                    detail="Invalid email or password."
                )

            print("LOGIN STEP 3")

            ok = verify_password(password, user.hashed_password)
            print("LOGIN STEP 4", ok)

            if not ok:
                raise HTTPException(
                    status_code=401,
                    detail="Invalid email or password."
                )

            print("LOGIN STEP 5")

            token = create_access_token(
                {
                    "sub": user.email,
                    "role": user.role
                }
            )

            print("LOGIN STEP 6")

            return {
                "access_token": token,
                "user": {
                    "name": user.full_name,
                    "email": user.email,
                    "role": user.role
                }
            }

        except Exception:
            traceback.print_exc()
            raise