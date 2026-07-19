from sqlalchemy.orm import Session
from app.models.finance import Finance


class FinanceRepository:

    @staticmethod
    def get_all(db: Session):
        return db.query(Finance).all()

    @staticmethod
    def get_latest(db: Session):
        return (
            db.query(Finance)
            .order_by(Finance.id.desc())
            .first()
        )