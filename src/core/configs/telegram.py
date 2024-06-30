from pydantic_settings import BaseSettings


class TelegramSettings(BaseSettings):
    TELEGRAM_API_KEY: str
    TELEGRAM_WEBHOOK_HOST: str
    TELEGRAM_WEBHOOK_PATH: str

    @property
    def TELEGRAM_WEB_HOOK(self) -> str:
        return f"{self.TELEGRAM_WEBHOOK_HOST}{self.TELEGRAM_WEBHOOK_PATH}"
