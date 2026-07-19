from app.rag.rag_pipeline import RAGPipeline

rag = RAGPipeline()

result = rag.ask(
    "What is the leave policy?"
)

print("=" * 60)
print("RAG PIPELINE TEST")
print("=" * 60)

print("\nAnswer:\n")
print(result["answer"])

print("\nSources:\n")

for source in result["sources"]:
    print(source)