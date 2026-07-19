from app.rag.document_manager import DocumentManager

manager = DocumentManager()

print("\nEnterprise RAG Directories\n")

for name, path in manager.directories().items():
    print(f"{name:12} -> {path}")