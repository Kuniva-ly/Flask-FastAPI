from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FastAPI App"
    debug: bool = True
    api_v1_prefix: str = "/api/v1"
    database_url: Optional[str] = "sqlite:///./test.db"
    secret_key: Optional[str] = "supersecretkey"

    class Config:
        env_file = ".env"


settings = Settings()
