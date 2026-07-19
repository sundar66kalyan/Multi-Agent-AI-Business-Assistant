from app.rag.pdf_loader import PDFLoader

loader = PDFLoader()
docs = loader.load_directory()

print("=" * 60)
print("PAGE SIZE")
print("=" * 60)

for i, doc in enumerate(docs, start=1):
    print(f"Page {i}: {len(doc.page_content)} characters")