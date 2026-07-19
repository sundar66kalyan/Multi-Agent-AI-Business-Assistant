from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.core.config import settings


class DocumentChunker:

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP,
            separators=["\n\n", "\n", ".", " ", ""]
        )

    def split(self, documents):

        return self.splitter.split_documents(documents)