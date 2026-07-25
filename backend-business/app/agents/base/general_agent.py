from sqlalchemy.orm import Session
import logging

from app.agents.base.base_agent import BaseAgent
from app.services.llm_service import LLMService
from app.services.ai_service import AIService  # Added import

# Configure logging
logger = logging.getLogger(__name__)


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

        # ---------- Try RAG Service ----------
        try:

            rag = AIService.ask(message)

            if rag.get("answer"):

                return {
                    "agent": self.name,
                    "success": True,
                    "answer": rag["answer"],
                    "source": "AI Service"
                }

        except Exception as e:

            logger.error(f"AI Service Error: {e}")

        # ---------- Fallback to Gemini ----------
        try:

            answer = self.llm.generate(message)

            return {
                "agent": self.name,
                "success": True,
                "answer": answer,
                "source": "Gemini"
            }

        except Exception as e:

            return {
                "agent": self.name,
                "success": False,
                "answer": f"Gemini Error: {str(e)}"
            }