from dataclasses import dataclass

from src.domain.entities.user import User
from src.domain.services.user import IFriendService, IUserService
from src.gateways.postgresql.models.user import UserORM
from src.gateways.postgresql.repositories.user import IUserRepository


@dataclass
class ORMUserService(IUserService, IFriendService):
    repository: IUserRepository

    async def get_or_create(self, user: User) -> User:
        user_dto = await self.repository.get_or_create(UserORM.from_entity(user))
        return user_dto.to_entity()

    async def add_friend(self, user: User, friend: User) -> None:
        user_dto = UserORM.from_entity(user)
        friend_dto = await self.repository.get_or_create(UserORM.from_entity(friend))
        await self.repository.add_friend(user_dto, friend_dto)
