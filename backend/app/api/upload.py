from pathlib import Path
import shutil

from fastapi import APIRouter, UploadFile, File, HTTPException

from app.rag.file_hash import calculate_sha256
from app.rag.duplicate_checker import DuplicateChecker
from app.rag.metadata_service import MetadataService
from app.rag.pdf_loader import PDFLoader
from app.rag.chunker import DocumentChunker
from app.rag.vector_store import VectorStoreManager
from app.core.config import settings

router = APIRouter(tags=["Upload"])


@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    upload_dir = Path(settings.UPLOAD_PATH)
    upload_dir.mkdir(parents=True, exist_ok=True)

    file_path = upload_dir / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    if DuplicateChecker.is_duplicate(str(file_path)):
        file_path.unlink(missing_ok=True)

        raise HTTPException(
            status_code=400,
            detail="Duplicate document detected."
        )

    loader = PDFLoader()

    docs = loader.load_pdf(str(file_path))

    chunker = DocumentChunker()

    chunks = chunker.split(docs)

    vector_store = VectorStoreManager()

    vector_store.add_documents(chunks)

    metadata = MetadataService()

    metadata.add_document(
        filename=file.filename,
        sha256=calculate_sha256(file_path),
        pages=len(docs),
        chunks=len(chunks),
        embedding_model=settings.EMBEDDING_MODEL
    )

    return {
        "success": True,
        "filename": file.filename,
        "pages": len(docs),
        "chunks": len(chunks),
        "message": "Document uploaded and indexed successfully."
    }