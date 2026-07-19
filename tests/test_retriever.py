from app.rag.retriever import Retriever

retriever = Retriever()

docs = retriever.search(
    "What is the leave policy?"
)

print("=" * 60)
print("RETRIEVER TEST")
print("=" * 60)

print(f"Retrieved Documents : {len(docs)}")

print()

for i, doc in enumerate(docs, start=1):

    print("=" * 30)
    print(f"Document {i}")
    print("=" * 30)

    print(doc.metadata)

    print()

    print(doc.page_content[:300])

    print()