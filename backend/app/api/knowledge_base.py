from fastapi import APIRouter

from app.rag.metadata_service import MetadataService

router = APIRouter(tags=["Knowledge Base"])


@router.get("/knowledge-base")
def knowledge_base():

    metadata = MetadataService()

    docs = metadata.load()

    return {
        "total_documents": len(docs),
        "documents": docs
    }