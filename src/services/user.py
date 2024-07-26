from dataclasses import dataclass

from src.domain.entities.user import User
from src.domain.services.user import IUserService
from src.gateways.postgresql.models.user import UserORM
from src.gateways.postgresql.repositories.user import IUserRepository


@dataclass
class ORMUserService(IUserService):
    repository: IUserRepository

    async def get_or_create(self, user: User) -> User:
        user_dto = await self.repository.get_or_create(UserORM.from_entity(user))
        return user_dto.to_entity()
