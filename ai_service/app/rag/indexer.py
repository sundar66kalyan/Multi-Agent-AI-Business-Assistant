from app.core.config import settings
from app.rag.loader import load_documents
from app.rag.splitter import split_documents
from app.rag.vectordb import VectorDB


class DocumentIndexer:

    def __init__(self):
        self.db = VectorDB()

    def index_documents(self):

        print("=" * 60)
        print("Loading documents...")
        print("=" * 60)

        documents = load_documents(
            settings.DOCUMENTS_DIR
        )

        print(f"Loaded {len(documents)} pages")

        if len(documents) == 0:
            return {
                "success": False,
                "message": "No PDF documents found."
            }

        chunks = split_documents(documents)

        print(f"Created {len(chunks)} chunks")

        self.db.add_documents(chunks)

        return {
            "success": True,
            "documents": len(documents),
            "chunks": len(chunks),
            "indexed": self.db.count()
        }