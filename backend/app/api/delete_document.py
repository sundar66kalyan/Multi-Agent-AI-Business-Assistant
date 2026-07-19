from pathlib import Path

from fastapi import APIRouter, HTTPException

from app.core.config import settings
from app.rag.metadata_service import MetadataService

router = APIRouter(tags=["Knowledge Base"])


@router.delete("/delete-document/{filename}")
def delete_document(filename: str):

    pdf = Path(settings.UPLOAD_PATH) / filename

    if pdf.exists():
        pdf.unlink()

    metadata = MetadataService()

    docs = metadata.load()

    exists = any(doc["filename"] == filename for doc in docs)

    if not exists:
        raise HTTPException(
            status_code=404,
            detail="Document not found."
        )

    metadata.delete_document(filename)

    return {
        "success": True,
        "message": f"{filename} deleted successfully."
    }