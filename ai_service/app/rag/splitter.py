from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.core.config import settings


_splitter = None


def get_splitter():
    """
    Returns a singleton text splitter.
    """

    global _splitter

    if _splitter is None:

        _splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

    return _splitter


def split_documents(documents):
    """
    Split documents into chunks.
    """

    splitter = get_splitter()

    return splitter.split_documents(documents)