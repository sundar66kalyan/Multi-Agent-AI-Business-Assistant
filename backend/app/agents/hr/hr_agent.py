from sqlalchemy.orm import Session

from app.agents.base.base_agent import BaseAgent
from app.rag.rag_pipeline import RAGPipeline

rag = None


class HRAgent(BaseAgent):

    @property
    def name(self):
        return "HR"

    def execute(
        self,
        message: str,
        db: Session = None
    ):
        global rag

        try:
            if rag is None:
                print("=" * 60)
                print("LOADING HR EMBEDDING MODEL")
                print("=" * 60)
                rag = RAGPipeline()

            print("=" * 60)
            print("CALLING RAG")
            print("QUESTION:", message)
            print("=" * 60)

            result = rag.ask(message)

            return {
                "agent": self.name,
                "success": True,
                "answer": result["answer"],
                "sources": result["sources"]
            }

        except Exception:
            import traceback

            print("=" * 80)
            print("HR AGENT ERROR")
            traceback.print_exc()
            print("=" * 80)
            raise