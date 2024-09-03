from uuid import UUID

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from src.domain.entities.user import User
from src.gateways.postgresql.models.base import BaseORM
from src.gateways.postgresql.models.mixins import UpdatedAtMixin, UUIDOidMixin


class UserORM(BaseORM, UUIDOidMixin, UpdatedAtMixin):
    __tablename__ = "user"

    telegram_id: Mapped[str | None] = mapped_column(sa.String(12), unique=True)
    first_name: Mapped[str | None] = mapped_column(sa.String(128))
    last_name: Mapped[str | None] = mapped_column(sa.String(128))
    username: Mapped[str] = mapped_column(sa.String(128))
    language_code: Mapped[str | None] = mapped_column(sa.String(8))

    @staticmethod
    def from_entity(entity: User) -> "UserORM":
        return UserORM(
            oid=entity.oid,
            telegram_id=entity.telegram_id,
            first_name=entity.first_name,
            last_name=entity.last_name,
            username=entity.username,
            language_code=entity.language_code,
        )

    def to_entity(self) -> User:
        return User(
            oid=self.oid,
            telegram_id=self.telegram_id,
            first_name=self.first_name,
            last_name=self.last_name,
            username=self.username,
            language_code=self.language_code,
        )


class FriendORM(BaseORM, UUIDOidMixin, UpdatedAtMixin):
    __tablename__ = "friend"

    user_oid: Mapped[UUID] = mapped_column(sa.ForeignKey("user.oid"))
    friend_oid: Mapped[UUID] = mapped_column(sa.ForeignKey("user.oid"))
    name: Mapped[str] = mapped_column(sa.String(128))
