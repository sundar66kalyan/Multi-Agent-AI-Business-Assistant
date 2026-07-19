from pathlib import Path

from app.rag.pdf_loader import PDFLoader


class RAGService:

    def __init__(self):

        self.loader = PDFLoader()

    def load_documents(self):

        return self.loader.load_directory()

    def total_documents(self):

        docs = self.load_documents()

        return len(docs)

    def status(self):

        return {
            "documents_loaded": self.total_documents(),
            "vector_database": Path("data/vector_db").exists(),
            "documents_folder": Path("data/documents").exists()
        }