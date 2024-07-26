from abc import ABC, abstractmethod
from dataclasses import dataclass

from sqlalchemy import select

from src.gateways.postgresql.database import Database
from src.gateways.postgresql.models.user import UserORM


class IUserRepository(ABC):
    @abstractmethod
    async def get_by_telegram_id(self, telegram_id: str) -> UserORM | None:
        pass

    @abstractmethod
    async def create(self, user: UserORM) -> UserORM:
        pass

    @abstractmethod
    async def get_or_create(self, user: UserORM) -> UserORM:
        pass


@dataclass
class ORMUserRepository(IUserRepository):
    database: Database

    async def get_by_telegram_id(self, telegram_id: str) -> UserORM | None:
        stmt = select(UserORM).where(UserORM.telegram_id == telegram_id).limit(1)
        async with self.database.get_read_only_session() as session:
            return await session.scalar(stmt)

    async def create(self, user: UserORM) -> UserORM:
        async with self.database.get_session() as session:
            session.add(user)
        return user

    async def get_or_create(self, user: UserORM) -> UserORM:
        db_user = await self.get_by_telegram_id(user.telegram_id)
        return db_user or await self.create(user)
