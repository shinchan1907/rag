from pydantic_settings import BaseSettings
from typing import List, Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "Jyoti AI"
    VERSION: str = "2.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Domain
    DOMAIN: str

    # Database
    DATABASE_URL: str
    
    # Redis
    REDIS_URL: str

    # OpenAI
    OPENAI_API_KEY: str
    
    # WhatsApp
    WHATSAPP_ACCESS_TOKEN: str
    WHATSAPP_VERIFY_TOKEN: str
    WHATSAPP_PHONE_NUMBER_ID: str
    
    # Owner
    OWNER_NUMBERS: str  # Comma separated

    @property
    def owner_list(self) -> List[str]:
        return [n.strip() for n in self.OWNER_NUMBERS.split(",")]

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
