from app.rag.pdf_loader import PDFLoader
from app.rag.vector_store import VectorStoreManager


def build_vector_database():

    print("=" * 60)
    print("INDEXING DOCUMENTS")
    print("=" * 60)

    loader = PDFLoader()

    docs = loader.load_directory()

    print(f"Loaded Pages : {len(docs)}")

    db = VectorStoreManager()

    db.add_documents(docs)

    print()

    print("Documents Indexed Successfully")

    print(f"Stored Chunks : {db.count()}")


if __name__ == "__main__":
    build_vector_database()