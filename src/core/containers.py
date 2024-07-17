from functools import lru_cache

import punq

from src.core.configs import settings
from src.domain.services.healthcheck import IHealthCheckService
from src.gateways.postgresql.database import Database
from src.services.healthcheck import (
    CompositeHealthcheckService,
    PostgresHealthcheckService,
)


@lru_cache(1)
def get_container() -> punq.Container:
    return _init_container()


def _init_container() -> punq.Container:
    container = punq.Container()

    container.register(
        Database,
        scope=punq.Scope.singleton,
        factory=lambda: Database(
            url=settings.POSTGRES_DB_URL, ro_url=settings.POSTGRES_DB_URL
        ),
    )

    container.register(PostgresHealthcheckService)

    def healthcheck_service_factory():
        services = [
            container.resolve(PostgresHealthcheckService),
        ]
        return CompositeHealthcheckService(services=services)

    container.register(IHealthCheckService, factory=healthcheck_service_factory)

    return container
