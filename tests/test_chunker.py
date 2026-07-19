from app.rag.pdf_loader import PDFLoader
from app.rag.chunker import DocumentChunker

loader = PDFLoader()
docs = loader.load_directory()

chunker = DocumentChunker()

chunks = chunker.split(docs)

print("=" * 60)
print("DOCUMENT CHUNKER")
print("=" * 60)

print("Original Pages :", len(docs))
print("Chunks Created :", len(chunks))

print("\nFirst Chunk:\n")
print(chunks[0].page_content[:500])