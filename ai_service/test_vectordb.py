from app.rag.vectordb import VectorDB

db = VectorDB()

print("=" * 60)
print("Documents:", db.count())
print("=" * 60)

docs = db.similarity_search("working hours", k=3)

print("Retrieved:", len(docs))

for i, doc in enumerate(docs, 1):
    print("=" * 60)
    print("Document", i)
    print(doc.page_content)