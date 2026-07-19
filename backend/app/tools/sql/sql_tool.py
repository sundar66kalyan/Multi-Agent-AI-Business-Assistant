from sqlalchemy.orm import Session

from app.repositories.finance_repository import FinanceRepository


class SQLTool:

    @staticmethod
    def latest_finance(db: Session):

        return FinanceRepository.get_latest(db)