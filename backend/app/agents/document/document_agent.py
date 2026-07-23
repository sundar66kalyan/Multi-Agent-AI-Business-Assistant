from sqlalchemy.orm import Session

from app.agents.base.base_agent import BaseAgent
from app.rag.rag_pipeline import RAGPipeline

rag = None

class DocumentAgent(BaseAgent):

    def __init__(self):
        global rag
        if rag is None:
            rag = RAGPipeline()

    @property
    def name(self):
        return "Document"

    def execute(
        self,
        message: str,
        db: Session = None
    ):

        result = rag.ask(message)

        return {
            "agent": self.name,
            "success": True,
            "answer": result["answer"],
            "sources": result["sources"]
        }