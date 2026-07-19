import bcrypt

from app.database.database import SessionLocal
from app.models.user import User

# Import database so tables are created
from app.database import database


db = SessionLocal()

try:
    # Don't insert duplicates if users already exist
    if db.query(User).count() == 0:

        users = [
            User(
                full_name="Administrator",
                username="admin",
                email="admin@example.com",
                hashed_password=bcrypt.hashpw(
                    "admin123".encode(),
                    bcrypt.gensalt()
                ).decode(),
                role="Administrator"
            ),

            User(
                full_name="Manager",
                username="manager",
                email="manager@example.com",
                hashed_password=bcrypt.hashpw(
                    "manager123".encode(),
                    bcrypt.gensalt()
                ).decode(),
                role="Manager"
            ),

            User(
                full_name="Business User",
                username="user",
                email="user@example.com",
                hashed_password=bcrypt.hashpw(
                    "user123".encode(),
                    bcrypt.gensalt()
                ).decode(),
                role="User"
            )
        ]

        db.add_all(users)
        db.commit()

        print("✅ Database created successfully.")
        print("✅ Demo users inserted.")

    else:
        print("Users already exist.")

finally:
    db.close()