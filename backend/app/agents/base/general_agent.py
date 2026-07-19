from sqlalchemy.orm import Session

from app.agents.base.base_agent import BaseAgent
from app.services.llm_service import LLMService


class GeneralAgent(BaseAgent):

    def __init__(self):
        self.llm = LLMService()

    @property
    def name(self):
        return "General"

    def execute(
        self,
        message: str,
        db: Session = None
    ):

        try:
            answer = self.llm.generate(message)

            return {
                "agent": self.name,
                "success": True,
                "answer": answer
            }

        except Exception as e:

            return {
                "agent": self.name,
                "success": False,
                "answer": f"Gemini Error: {str(e)}"
            }