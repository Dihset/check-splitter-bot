from src.core.configs.telegram import TelegramSettings


class Settings(TelegramSettings):
    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
