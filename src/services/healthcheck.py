from dataclasses import dataclass

import sqlalchemy as sa
from sqlalchemy.exc import SQLAlchemyError

from src.domain.services.healthcheck import IHealthCheckService
from src.gateways.postgresql.database import Database
from src.utils.aio import gather_and_wait


@dataclass
class PostgresHealthcheckService(IHealthCheckService):
    database: Database

    async def check(self) -> dict[str, bool]:
        async with self.database.get_read_only_session() as session:
            try:
                cursor = await session.execute(sa.select(1))
                result = cursor.scalar()
                return {self.__class__.__name__: result == 1}
            except SQLAlchemyError:
                raise


@dataclass
class CompositeHealthcheckService(IHealthCheckService):
    services: list[IHealthCheckService]

    async def check(self) -> dict[str, bool]:
        results = await gather_and_wait([service.check() for service in self.services])

        ans = {}
        for result in results:
            ans.update(result)

        return ans
