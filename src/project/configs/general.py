from enum import Enum

from pydantic_settings import BaseSettings


class Environment(str, Enum):
    DEV = "dev"
    PROD = "prod"
    LOCAL = "local"


class GeneralSettings(BaseSettings):
    SERVICE_NAME: str = "check-splitter"
    ENVIRONMENT: Environment = Environment.DEV
