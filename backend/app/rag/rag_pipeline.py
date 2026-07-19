from app.rag.retriever import Retriever
from app.rag.prompt import SYSTEM_PROMPT
from app.services.llm_service import LLMService


class RAGPipeline:

    def __init__(self):
        self.retriever = Retriever()
        self.llm = LLMService()

    def ask(self, question: str):

        docs = self.retriever.search(question)

        if not docs:
            return {
                "answer": "No relevant documents found.",
                "sources": []
            }

        context = "\n\n".join(doc.page_content for doc in docs)

        prompt = SYSTEM_PROMPT.format(
            context=context,
            question=question
        )

        answer = self.llm.generate(prompt)

        sources = []

        for doc in docs:
            sources.append({
                "document": doc.metadata.get("source"),
                "page": doc.metadata.get("page")
            })

        return {
            "answer": answer,
            "sources": sources
        }