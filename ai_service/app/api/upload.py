from fastapi import APIRouter, UploadFile, File
from pathlib import Path
import shutil
import traceback

from app.rag.indexer import DocumentIndexer

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

UPLOAD_DIR = Path("data/documents")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/")
def upload_pdf(file: UploadFile = File(...)):
    try:
        print("=" * 80)
        print("UPLOAD STARTED")

        destination = UPLOAD_DIR / file.filename

        print("Saving:", destination)

        with open(destination, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        print("Saved")

        indexer = DocumentIndexer()

        print("Indexer created")

        result = indexer.index_documents()

        print(result)

        return {
            "success": True,
            "result": result
        }

    except Exception:
        traceback.print_exc()
        raise