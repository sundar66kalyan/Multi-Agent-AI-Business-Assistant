from pathlib import Path

from langchain_chroma import Chroma

from app.core.config import settings
from app.rag.embeddings import get_embeddings


_db = None


def get_vectordb():
    """
    Returns a singleton Chroma database.
    """

    global _db

    if _db is None:

        Path(settings.VECTOR_DB_DIR).mkdir(
            parents=True,
            exist_ok=True
        )

        _db = Chroma(
            collection_name="business_documents",
            persist_directory=settings.VECTOR_DB_DIR,
            embedding_function=get_embeddings(),
        )

    return _db


class VectorDB:

    def __init__(self):
        self.db = get_vectordb()

    def add_documents(self, documents):
        self.db.add_documents(documents)

    def similarity_search(self, query, k=None):

        if k is None:
            k = settings.TOP_K

        return self.db.similarity_search(
            query,
            k=k
        )

    def get_retriever(self):

        return self.db.as_retriever(
            search_kwargs={
                "k": settings.TOP_K
            }
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
            embedding_function=get_embeddings(),
        )

        self.db = _db