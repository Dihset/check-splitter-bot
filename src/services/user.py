from ast import List
from dataclasses import dataclass
from uuid import UUID

from sqlalchemy import select

from src.domain.entities.user import User
from src.domain.services.user import IFriendService, IUserService
from src.gateways.postgresql.database import Database
from src.gateways.postgresql.models.user import FriendORM, UserORM


@dataclass
class ORMUserService(IUserService, IFriendService):
    database: Database

    async def create(self, user: User) -> User:
        user_dto = UserORM.from_entity(user)
        async with self.database.get_session() as session:
            session.add(user_dto)
        return user_dto.to_entity()

    async def get_by_telegram(self, telegram_id: str) -> User | None:
        stmt = select(UserORM).where(UserORM.telegram_id == telegram_id).limit(1)
        async with self.database.get_read_only_session() as session:
            user_dto = await session.scalar(stmt)
            if not user_dto:
                return None
            return user_dto.to_entity()

    async def get_by_oid(self, oid: str) -> User | None:
        stmt = select(UserORM).where(UserORM.oid == oid).limit(1)
        async with self.database.get_read_only_session() as session:
            user_dto = await session.scalar(stmt)
            if not user_dto:
                return None
            return user_dto.to_entity()

    async def get_or_create(self, user: User) -> User:
        ans_user = await self.get_by_oid(user.oid)
        if not ans_user:
            return await self.create(user)
        return ans_user

    async def add_friend(self, user: User, friend: User) -> None:
        user = UserORM.from_entity(user)
        friend = await self.get_or_create(friend)
        async with self.database.get_session() as session:
            session.add(
                FriendORM(
                    user_oid=user.oid,
                    friend_oid=friend.oid,
                    name=friend.username,
                )
            )
            session.add(
                FriendORM(
                    user_oid=friend.oid,
                    friend_oid=user.oid,
                    name=user.username,
                )
            )

    async def get_friends(self, user_oid: UUID) -> List:
        stmt = (
            select(UserORM)
            .join(FriendORM, FriendORM.friend_oid == UserORM.oid)
            .where(FriendORM.user_oid == user_oid)
        )
        async with self.database.get_read_only_session() as session:
            friens_dto = await session.execute(stmt)
            return [friend_dto.to_entity() for friend_dto, *_ in friens_dto]
