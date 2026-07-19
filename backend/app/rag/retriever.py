from app.rag.vector_store import VectorStoreManager


class Retriever:

    def __init__(self):
        self.vector_store = VectorStoreManager()
        self.retriever = self.vector_store.get_retriever()

    def search(self, question: str):

        docs = self.retriever.invoke(question)

        return docs