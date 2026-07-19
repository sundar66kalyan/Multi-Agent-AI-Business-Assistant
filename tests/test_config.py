from app.core.config import settings

print("=" * 60)
print("CONFIGURATION")
print("=" * 60)

print(settings.LLM_MODEL)
print(settings.EMBEDDING_MODEL)
print(settings.DOCUMENTS_DIR)
print(settings.VECTOR_DB_DIR)
print(settings.TOP_K)