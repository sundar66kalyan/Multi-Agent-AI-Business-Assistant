import time

from langchain_huggingface import HuggingFaceEmbeddings

from app.core.config import settings


_embedding_model = None


def get_embedding_model():
    """
    Singleton embedding model.
    Loaded only once for the entire application.
    """

    global _embedding_model

    if _embedding_model is not None:
        return _embedding_model

    print("=" * 60)
    print("LOADING EMBEDDING MODEL")
    print("=" * 60)

    start = time.perf_counter()

    _embedding_model = HuggingFaceEmbeddings(
        model_name=settings.EMBEDDING_MODEL,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )

    end = time.perf_counter()

    print(f"Loading Time : {end-start:.2f} sec")
    print("=" * 60)

    return _embedding_model