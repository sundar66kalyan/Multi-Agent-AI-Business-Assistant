from langchain_chroma import Chroma

from app.core.config import settings
from app.rag.embedding_service import get_embedding_model


# -----------------------------
# Global singleton objects
# -----------------------------
_db = None


def get_vector_db():
    global _db

    if _db is None:
        print("=" * 60)
        print("INITIALIZING CHROMA DATABASE")
        print("=" * 60)

        _db = Chroma(
            collection_name="business_documents",
            persist_directory=settings.VECTOR_DB_DIR,
            embedding_function=get_embedding_model(),
        )

    return _db


class VectorStoreManager:

    def __init__(self):
        self.db = get_vector_db()

    def add_documents(self, documents):
        self.db.add_documents(documents)

    def get_retriever(self):
        return self.db.as_retriever(
            search_kwargs={"k": settings.TOP_K}
        )

    def count(self):
        return self.db._collection.count()

    def reset(self):

        global _db

        try:
            self.db.delete_collection()
        except Exception:
            pass

        _db = Chroma(
            collection_name="business_documents",
            persist_directory=settings.VECTOR_DB_DIR,
            embedding_function=get_embedding_model(),
        )

        self.db = _db