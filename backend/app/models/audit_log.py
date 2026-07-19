from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from app.database.database import Base


class AuditLog(Base):
    """
    Stores all user actions performed inside the application.
    """

    __tablename__ = "audit_logs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String,
        nullable=False
    )

    action = Column(
        String,
        nullable=False
    )

    target = Column(
        String,
        nullable=True
    )

    timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )