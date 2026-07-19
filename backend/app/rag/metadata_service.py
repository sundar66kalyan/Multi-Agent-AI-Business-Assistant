# app/rag/metadata_service.py

import json
from pathlib import Path
from datetime import datetime


class MetadataService:

    METADATA_FILE = Path("data/metadata/documents.json")

    def __init__(self):

        self.METADATA_FILE.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if not self.METADATA_FILE.exists():
            self.METADATA_FILE.write_text("[]")

    def load(self):
        return json.loads(
            self.METADATA_FILE.read_text(
                encoding="utf-8"
            )
        )

    def save(self, data):
        self.METADATA_FILE.write_text(
            json.dumps(
                data,
                indent=4
            ),
            encoding="utf-8"
        )

    def add_document(
        self,
        filename,
        sha256,
        pages,
        chunks,
        embedding_model
    ):
        docs = self.load()

        docs.append({
            "id": len(docs) + 1,
            "filename": filename,
            "sha256": sha256,
            "pages": pages,
            "chunks": chunks,
            "embedding_model": embedding_model,
            "indexed": True,
            "uploaded_at": datetime.now().isoformat()
        })

        self.save(docs)

    def delete_document(self, filename: str):
        """
        Delete a document from metadata by filename.
        
        Args:
            filename (str): Name of the document to delete
        """
        docs = self.load()

        docs = [
            doc
            for doc in docs
            if doc["filename"] != filename
        ]

        self.save(docs)