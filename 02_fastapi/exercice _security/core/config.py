from typing import Optional
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    app_name: str = Field("BABY Foot Application", alias="APP_NAME")
    debug: bool = Field(False, alias="DEBUG")
    database_url: Optional[str] = Field(None, alias="DATABASE_URL")
    secret_key: str = Field("Change-Me-Please", alias="SECRET_KEY")
    token_expire_minutes: int = Field(30, alias="TOKEN_EXPIRE_MINUTES")
    api_prefix: str = Field("/api", alias="API_PREFIX")
    log_level: str = Field("INFO", alias="LOG_LEVEL")

    model_config = SettingsConfigDict(env_file=".env", 
                                       env_file_encoding="utf-8",
                                       case_sensitive=False,
                                       extra="ignore"
                                       )
settings = Settings()