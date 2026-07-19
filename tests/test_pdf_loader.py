from app.rag.pdf_loader import PDFLoader

loader = PDFLoader()

docs = loader.load_directory()

print("\n" + "=" * 60)
print("Enterprise PDF Loader")
print("=" * 60)

print(f"Total Pages Loaded: {len(docs)}\n")

if docs:
    print("First Page Preview:\n")
    print(docs[0].page_content[:500])

    print("\nMetadata:")
    print(docs[0].metadata)
else:
    print("No documents found.")