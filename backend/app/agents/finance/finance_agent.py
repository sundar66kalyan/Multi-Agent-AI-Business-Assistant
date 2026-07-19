from sqlalchemy.orm import Session

from app.agents.base.base_agent import BaseAgent
from app.services.finance_service import FinanceService


class FinanceAgent(BaseAgent):

    @property
    def name(self):
        return "Finance"

    def execute(
        self,
        message: str,
        db: Session = None
    ):

        answer = FinanceService.answer_question(
            db,
            message
        )

        return {
            "agent": self.name,
            "success": True,
            "message": "Finance request completed.",
            "data": answer
        }