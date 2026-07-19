import bcrypt

from app.database.database import SessionLocal
from app.models.user import User
from app.core.security import get_password_hash

# Import database so tables are created
from app.database import database


def seed_demo_users():
    db = SessionLocal()

    demo_users = [
        {
            "full_name": "Administrator",
            "email": "admin@example.com",
            "password": "admin123",
            "role": "Administrator",
        },
        {
            "full_name": "Manager",
            "email": "manager@example.com",
            "password": "manager123",
            "role": "Manager",
        },
        {
            "full_name": "Business User",
            "email": "user@example.com",
            "password": "user123",
            "role": "User",
        },
    ]

    for demo in demo_users:
        user = db.query(User).filter(User.email == demo["email"]).first()

        if user:
            user.full_name = demo["full_name"]
            user.role = demo["role"]
            user.hashed_password = get_password_hash(demo["password"])
        else:
            db.add(
                User(
                    full_name=demo["full_name"],
                    email=demo["email"],
                    hashed_password=get_password_hash(demo["password"]),
                    role=demo["role"],
                )
            )

    db.commit()
    db.close()


# Run seeding if this script is executed directly
if __name__ == "__main__":
    db = SessionLocal()
    
    try:
        # Don't insert duplicates if users already exist
        if db.query(User).count() == 0:
            seed_demo_users()
            print("✅ Database created successfully.")
            print("✅ Demo users inserted.")
        else:
            print("Users already exist.")
    finally:
        db.close()