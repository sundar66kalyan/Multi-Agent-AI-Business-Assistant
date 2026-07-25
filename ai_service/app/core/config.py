from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str = "AI Service"
    APP_VERSION: str = "1.0.0"

    GROQ_API_KEY: str = ""

    LLM_MODEL: str = "llama-3.3-70b-versatile"

    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"

    DOCUMENTS_DIR: str = "data/documents"
    VECTOR_DB_DIR: str = "data/vector_db"

    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 200
    TOP_K: int = 3

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()