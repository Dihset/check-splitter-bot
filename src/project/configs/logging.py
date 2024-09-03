import logging

import ecs_logging

from src.project.configs.general import Environment, GeneralSettings


class LoggingSettings(GeneralSettings):
    ELASTIC_APM_SERVER: str | None = None

    @property
    def ELASTIC_APM(self) -> dict[str, str]:
        return {
            "SERVICE_NAME": self.SERVICE_NAME,
            "SERVER_URL": self.ELASTIC_APM_SERVER,
            "ENVIRONMENT": self.ENVIRONMENT,
            "CAPTURE_BODY": "all",
        }

    def config_server_logger(self):
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        handler = logging.StreamHandler()
        handler.setFormatter(ecs_logging.StdlibFormatter())
        logger.addHandler(handler)

    def config_local_logger(self):
        logging.basicConfig(level=logging.DEBUG)

    def config_logger(self):
        if self.ENVIRONMENT == Environment.LOCAL:
            self.config_local_logger()
        else:
            self.config_server_logger()
