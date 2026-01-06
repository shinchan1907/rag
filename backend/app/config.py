from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # OpenAI
    OPENAI_API_KEY: str

    # WhatsApp
    WHATSAPP_ACCESS_TOKEN: str
    WHATSAPP_BUSINESS_ACCOUNT_ID: str
    WHATSAPP_PHONE_NUMBER_ID: str
    WHATSAPP_PHONE_NUMBER: str
    WHATSAPP_WEBHOOK_VERIFY_TOKEN: str

    # Owners
    OWNER_NUMBERS: List[str] = ["919872944859", "917087215463"]

    # Database
    DATABASE_URL: str
    
    # Vector DB
    CHROMA_DB_PATH: str = "./chroma_db"

    # Redis
    REDIS_URL: str = "redis://redis:6379/0"

    # Domain
    DOMAIN: str = "ai.bytenex.io"

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
