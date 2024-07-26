from abc import ABC, abstractmethod

from src.domain.entities.user import User


class IUserService(ABC):
    @abstractmethod
    async def get_or_create(self, user: User) -> User:
        pass
