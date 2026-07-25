from langchain_huggingface import HuggingFaceEmbeddings

from app.core.config import settings


_embedding = None


def get_embeddings():
    """
    Returns a singleton HuggingFace embedding model.
    """

    global _embedding

    if _embedding is None:

        _embedding = HuggingFaceEmbeddings(
            model_name=settings.EMBEDDING_MODEL,
            model_kwargs={
                "device": "cpu"
            },
            encode_kwargs={
                "normalize_embeddings": True
            }
        )

    return _embedding