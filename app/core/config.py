from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import dotenv_values
from pydantic import SecretStr

class Settings(BaseSettings):
    # LLM Configuration
    GROQ_API_KEY: str = ""
    TAVILY_API_KEY: str = ""
    
    # FastAPI Configuration
    SECRET_KEY: str = ""
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 200

    # Database Configuration
    # Async URL (postgresql+asyncpg)
    DATABASE_URL: str = ""  
    DATABASE_URL_ALEMBIC: str = ""
    DB_ROLE_NAME: str 
    DB_PASSWORD: str 
    DB_HOST: str 
    DATABASE: str 
    DB_PORT: int 

    #Mail Configuration:
    MAIL_USERNAME: str 
    MAIL_PASSWORD: SecretStr 
    MAIL_FROM: str 
    MAIL_PORT: int 
    MAIL_SERVER: str 
    MAIL_FROM_NAME : str 

    model_config  = SettingsConfigDict(env_file="app/.env",extra="ignore")
     


CONFIG = Settings()

# async database url secction:
CONFIG.DATABASE_URL = (
    f"postgresql+asyncpg://{CONFIG.DB_ROLE_NAME}:{CONFIG.DB_PASSWORD}"
    f"@{CONFIG.DB_HOST}:{CONFIG.DB_PORT}/{CONFIG.DATABASE}"
)

CONFIG.DATABASE_URL_ALEMBIC = (
    f"postgresql://{CONFIG.DB_ROLE_NAME}:{CONFIG.DB_PASSWORD}"
    f"@{CONFIG.DB_HOST}:{CONFIG.DB_PORT}/{CONFIG.DATABASE}"
) 

