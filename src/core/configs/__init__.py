from src.core.configs.database import PostgresSettings
from src.core.configs.general import GeneralSettings
from src.core.configs.logging import LoggingSettings
from src.core.configs.telegram import TelegramSettings


class Settings(
    PostgresSettings,
    TelegramSettings,
    LoggingSettings,
    GeneralSettings,
):
    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
