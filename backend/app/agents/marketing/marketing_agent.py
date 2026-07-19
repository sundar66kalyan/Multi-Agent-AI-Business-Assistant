from sqlalchemy.orm import Session

from app.agents.base.base_agent import BaseAgent
from app.services.llm_service import LLMService


class MarketingAgent(BaseAgent):

    @property
    def name(self):
        return "Marketing"

    def execute(
        self,
        message: str,
        db: Session = None
    ):

        llm = LLMService()

        prompt = f"""
You are an expert Marketing AI Assistant.

Generate professional marketing content.

User Request:
{message}
"""

        answer = llm.generate(prompt)

        return {
            "agent": self.name,
            "success": True,
            "answer": answer
        }