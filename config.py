from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    TELEGRAM_TOKEN: str = Field(..., description="Telegram Bot API token")
    DATABASE_URL: str = Field(
        default="sqlite+aiosqlite:///./fitcoach.db",
        description="SQLAlchemy URL, e.g. postgresql+asyncpg://user:pass@host/db",
    )
    ADMIN_IDS: list[int] = Field(default_factory=list, description="Telegram user IDs of admins")
    LOG_LEVEL: str = Field(default="INFO")
    TIMEZONE: str = Field(default="Europe/Warsaw")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings()
