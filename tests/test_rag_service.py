from app.services.rag_service import RAGService

rag = RAGService()

print("=" * 60)
print("RAG Service")
print("=" * 60)

print(rag.status())