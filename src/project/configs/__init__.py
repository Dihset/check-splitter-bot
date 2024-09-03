from src.project.configs.database import PostgresSettings
from src.project.configs.general import GeneralSettings
from src.project.configs.logging import LoggingSettings
from src.project.configs.telegram import TelegramSettings


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
