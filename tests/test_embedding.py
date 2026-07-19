from app.rag.embedding_service import get_embedding_model

model = get_embedding_model()

text = "Artificial Intelligence is transforming businesses."

vector = model.embed_query(text)

print("=" * 60)
print("Embedding Test")
print("=" * 60)

print(f"Vector Dimension : {len(vector)}")

print()

print(vector[:10])