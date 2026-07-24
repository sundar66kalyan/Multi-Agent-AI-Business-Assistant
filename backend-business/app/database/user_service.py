import bcrypt
from app.database.database import SessionLocal
from app.models.user import User
from sqlalchemy.exc import IntegrityError


class UserService:

    @staticmethod
    def get_all_users():
        """Get all users from the database."""
        db = SessionLocal()
        users = db.query(User).all()
        db.close()
        return users

    @staticmethod
    def create_user(full_name, username, email, password, role):
        """
        Create a new user with bcrypt password hashing.
        
        Args:
            full_name (str): User's full name
            username (str): User's username (unique)
            email (str): User's email address (unique)
            password (str): Plain text password (will be hashed with bcrypt)
            role (str): User role (Administrator, Manager, User)
            
        Returns:
            dict: Success status and user object or error message
        """
        db = SessionLocal()

        try:
            # Check if user already exists by email OR username
            existing = (
                db.query(User)
                .filter(
                    (User.email == email) |
                    (User.username == username)
                )
                .first()
            )

            if existing:
                # Determine which field caused the conflict
                if existing.email == email:
                    return {
                        "success": False,
                        "message": "Email already exists."
                    }
                elif existing.username == username:
                    return {
                        "success": False,
                        "message": "Username already exists."
                    }
                else:
                    return {
                        "success": False,
                        "message": "User already exists."
                    }

            # Hash the password using bcrypt
            hashed_password = bcrypt.hashpw(
                password.encode(),
                bcrypt.gensalt()
            ).decode()

            # Create new user with username field
            user = User(
                full_name=full_name,
                username=username,
                email=email,
                hashed_password=hashed_password,
                role=role
            )

            db.add(user)
            db.commit()
            db.refresh(user)

            print(f"✅ User created successfully: {user.full_name} (Username: {user.username}, Email: {user.email})")

            return {
                "success": True,
                "user": user
            }

        except IntegrityError:
            db.rollback()
            print("❌ IntegrityError: Duplicate username or email.")
            return {
                "success": False,
                "message": "Duplicate username or email."
            }

        except Exception as e:
            db.rollback()
            print(f"❌ Error creating user: {e}")
            import traceback
            traceback.print_exc()

            return {
                "success": False,
                "message": str(e)
            }

        finally:
            db.close()

    @staticmethod
    def delete_user(user_id):
        """
        Delete a user by ID.
        
        Args:
            user_id (int): ID of the user to delete
        """
        db = SessionLocal()

        user = db.query(User).filter(
            User.id == user_id
        ).first()

        if user:
            db.delete(user)
            db.commit()
            print(f"🗑️ User deleted: {user.full_name} (ID: {user_id})")

        db.close()

    # ============================================================
    # RESET PASSWORD
    # ============================================================

    @staticmethod
    def reset_password(user_id, new_password):
        """
        Reset a user's password with bcrypt hashing.
        
        Args:
            user_id (int): User's ID
            new_password (str): New plain text password (will be hashed with bcrypt)
            
        Returns:
            dict: Success status and message
        """
        db = SessionLocal()

        try:
            user = db.query(User).filter(
                User.id == user_id
            ).first()

            if not user:
                return {
                    "success": False,
                    "message": "User not found."
                }

            # Hash the new password using bcrypt
            user.hashed_password = bcrypt.hashpw(
                new_password.encode(),
                bcrypt.gensalt()
            ).decode()

            db.commit()

            print(f"✅ Password reset successfully for: {user.full_name} (ID: {user_id})")

            return {
                "success": True,
                "message": "Password updated successfully."
            }

        except Exception as e:
            db.rollback()
            print(f"❌ Error resetting password: {e}")
            return {
                "success": False,
                "message": f"Error: {str(e)}"
            }

        finally:
            db.close()

    @staticmethod
    def get_user_by_email(email):
        """
        Get a user by email address.
        
        Args:
            email (str): User's email address
            
        Returns:
            User: User object or None if not found
        """
        db = SessionLocal()

        user = db.query(User).filter(
            User.email == email
        ).first()

        db.close()

        if user:
            print(f"👤 User found: {user.full_name} ({user.email})")
        else:
            print(f"❌ No user found with email: {email}")

        return user

    @staticmethod
    def get_user_by_username(username):
        """
        Get a user by username.
        
        Args:
            username (str): User's username
            
        Returns:
            User: User object or None if not found
        """
        db = SessionLocal()

        user = db.query(User).filter(
            User.username == username
        ).first()

        db.close()

        if user:
            print(f"👤 User found: {user.full_name} (Username: {user.username})")
        else:
            print(f"❌ No user found with username: {username}")

        return user

    @staticmethod
    def get_user_by_id(user_id):
        """
        Get a user by ID.
        
        Args:
            user_id (int): User's ID
            
        Returns:
            User: User object or None if not found
        """
        db = SessionLocal()

        user = db.query(User).filter(
            User.id == user_id
        ).first()

        db.close()

        if user:
            print(f"👤 User found: {user.full_name} (ID: {user_id})")
        else:
            print(f"❌ No user found with ID: {user_id}")

        return user

    @staticmethod
    def update_user(user_id, full_name=None, username=None, email=None, role=None, password=None):
        """
        Update user information.
        
        Args:
            user_id (int): User's ID
            full_name (str, optional): New full name
            username (str, optional): New username
            email (str, optional): New email address
            role (str, optional): New role
            password (str, optional): New plain text password (will be hashed with bcrypt)
            
        Returns:
            dict: Success status and user object or error message
        """
        db = SessionLocal()

        try:
            user = db.query(User).filter(
                User.id == user_id
            ).first()

            if not user:
                return {
                    "success": False,
                    "message": "User not found."
                }

            # Update full name if provided
            if full_name is not None:
                user.full_name = full_name
            
            # Update username if provided (with uniqueness check)
            if username is not None:
                existing = (
                    db.query(User)
                    .filter(User.username == username)
                    .filter(User.id != user_id)
                    .first()
                )
                if existing:
                    return {
                        "success": False,
                        "message": "Username already exists."
                    }
                user.username = username
            
            # Update email if provided (with uniqueness check)
            if email is not None:
                existing = (
                    db.query(User)
                    .filter(User.email == email)
                    .filter(User.id != user_id)
                    .first()
                )
                if existing:
                    return {
                        "success": False,
                        "message": "Email already exists."
                    }
                user.email = email
            
            # Update role if provided
            if role is not None:
                user.role = role
            
            # Update password if provided (hash with bcrypt)
            if password:
                user.hashed_password = bcrypt.hashpw(
                    password.encode(),
                    bcrypt.gensalt()
                ).decode()

            # Commit changes to database
            db.commit()
            db.refresh(user)

            print(f"✅ User updated: {user.full_name} (ID: {user_id})")

            return {
                "success": True,
                "user": user
            }

        except IntegrityError as e:
            db.rollback()
            print(f"❌ IntegrityError: {e}")
            return {
                "success": False,
                "message": "Database integrity error."
            }

        except Exception as e:
            db.rollback()
            print(f"❌ Unexpected error: {e}")
            return {
                "success": False,
                "message": f"Error: {str(e)}"
            }

        finally:
            db.close()