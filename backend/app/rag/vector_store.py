from langchain_chroma import Chroma

from app.core.config import settings
from app.rag.embedding_service import get_embedding_model


class VectorStoreManager:

    def __init__(self):

        self.db = Chroma(
            collection_name="business_documents",
            persist_directory=settings.VECTOR_DB_DIR,
            embedding_function=get_embedding_model(),
        )

    def add_documents(self, documents):

        self.db.add_documents(documents)

    def get_retriever(self):

        return self.db.as_retriever(
            search_kwargs={"k": settings.TOP_K}
        )

    def count(self):

        return self.db._collection.count()

    def reset(self):

        try:
            self.db.delete_collection()
        except Exception:
            pass

        self.db = Chroma(
            collection_name="business_documents",
            persist_directory=settings.VECTOR_DB_DIR,
            embedding_function=get_embedding_model(),
        )