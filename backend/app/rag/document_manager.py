from pathlib import Path


class DocumentManager:

    def __init__(self):

        self.base = Path("data")

        self.documents = self.base / "documents"

        self.uploads = self.base / "uploads"

        self.metadata = self.base / "metadata"

        self.vector_db = self.base / "vector_db"

        self.processed = self.base / "processed"

        self.cache = self.base / "cache"

    def directories(self):

        return {
            "documents": str(self.documents),
            "uploads": str(self.uploads),
            "metadata": str(self.metadata),
            "vector_db": str(self.vector_db),
            "processed": str(self.processed),
            "cache": str(self.cache)
        }