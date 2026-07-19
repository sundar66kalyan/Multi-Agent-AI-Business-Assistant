from app.rag.vector_store import VectorStoreManager

db = VectorStoreManager()

print("=" * 60)
print("VECTOR STORE")
print("=" * 60)

print("Collection Name :", "business_documents")
print("Stored Chunks   :", db.count())