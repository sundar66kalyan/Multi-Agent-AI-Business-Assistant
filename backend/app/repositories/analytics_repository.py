from sqlalchemy.orm import Session

from app.models.finance import Finance


class AnalyticsRepository:

    @staticmethod
    def total_finance_records(db: Session):

        return db.query(Finance).count()