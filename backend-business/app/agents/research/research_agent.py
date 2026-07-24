from sqlalchemy.orm import Session

from app.agents.base.base_agent import BaseAgent
from app.services.llm_service import LLMService


class ResearchAgent(BaseAgent):

    @property
    def name(self):
        return "Research"

    def execute(
        self,
        message: str,
        db: Session = None
    ):

        llm = LLMService()

        prompt = f"""
You are an AI Research Assistant.

Provide a factual, well-structured answer.

Question:
{message}
"""

        answer = llm.generate(prompt)

        return {
            "agent": self.name,
            "success": True,
            "answer": answer
        }