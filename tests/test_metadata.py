from app.rag.metadata_service import MetadataService

metadata = MetadataService()

metadata.add_document(

    filename="Employee Handbook.pdf",

    sha256="123456789",

    pages=7,

    chunks=7,

    embedding_model="all-MiniLM-L6-v2"

)

print("=" * 60)
print("METADATA TEST")
print("=" * 60)

for doc in metadata.load():

    print(doc)