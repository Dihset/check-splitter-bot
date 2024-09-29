from abc import ABC, abstractmethod
from uuid import UUID

from src.domain.entities.user import User


class IUserService(ABC):
    @abstractmethod
    async def create(self, user: User) -> User:
        pass

    @abstractmethod
    async def get_by_telegram(self, telegram_id: str) -> User | None:
        pass

    @abstractmethod
    async def get_by_oid(self, oid: UUID) -> User | None:
        pass

    @abstractmethod
    async def get_or_create(self, user: User) -> User:
        pass


class IFriendService(ABC):
    @abstractmethod
    async def add_friend(self, user: User, friend: User) -> None:
        pass

    @abstractmethod
    async def get_friends(self, user_oid: UUID) -> list[User]:
        pass
