from app.database.database import SessionLocal
from app.models.audit_log import AuditLog


class AuditService:

    @staticmethod
    def log(user, action, target):

        db = SessionLocal()

        log = AuditLog(
            user=user,
            action=action,
            target=target
        )

        db.add(log)

        db.commit()

        db.close()