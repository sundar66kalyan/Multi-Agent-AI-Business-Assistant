from sqlalchemy.orm import Session

from app.agents.base.base_agent import BaseAgent


class SalesAgent(BaseAgent):

    @property
    def name(self):
        return "Sales"

    def execute(
        self,
        message: str,
        db: Session = None
    ):

        return {
            "agent": self.name,
            "success": True,
            "message": "Sales request completed.",
            "data": {
                "query": message
            }
        }