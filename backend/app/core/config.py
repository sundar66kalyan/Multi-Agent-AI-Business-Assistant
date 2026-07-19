from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):

    # -----------------------------
    # Application
    # -----------------------------
    APP_NAME: str = "Multi-Agent AI Business Assistant"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    HOST: str = "127.0.0.1"
    PORT: int = 8000

    # -----------------------------
    # API Keys
    # -----------------------------
    GOOGLE_API_KEY: str = ""
    GROQ_API_KEY: str = ""

    # -----------------------------
    # Database
    # -----------------------------
    DATABASE_URL: str = "sqlite:///./business_assistant.db"

    # -----------------------------
    # JWT
    # -----------------------------
    JWT_SECRET_KEY: str = ""
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # -----------------------------
    # RAG
    # -----------------------------
    LLM_MODEL: str = "llama-3.3-70b-versatile"
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"

    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 200
    TOP_K: int = 3

    DOCUMENTS_DIR: str = str(BASE_DIR / "data" / "documents")
    VECTOR_DB_DIR: str = str(BASE_DIR / "data" / "vector_db")
    METADATA_DIR: str = str(BASE_DIR / "data" / "metadata")
    UPLOAD_PATH: str = str(BASE_DIR / "data" / "uploads")

    # Legacy .env compatibility
    CHROMA_DB_PATH: str = "data/vector_db"
    DOCUMENT_PATH: str = "data/documents"
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"   # Ignore unknown variables instead of failing
    )


settings = Settings()