import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from src.domain.entities.user import User
from src.gateways.postgresql.models.base import BaseORM
from src.gateways.postgresql.models.mixins import UpdatedAtMixin, UUIDOidMixin


class UserORM(BaseORM, UUIDOidMixin, UpdatedAtMixin):
    __tablename__ = "user"

    telegram_id: Mapped[str] = mapped_column(sa.String(12), unique=True)
    first_name: Mapped[str | None] = mapped_column(sa.String(128))
    last_name: Mapped[str | None] = mapped_column(sa.String(128))
    username: Mapped[str | None] = mapped_column(sa.String(128))
    language_code: Mapped[str | None] = mapped_column(sa.String(8))

    @staticmethod
    def from_entity(obj: User) -> "UserORM":
        return UserORM(
            telegram_id=obj.telegram_id,
            first_name=obj.first_name,
            last_name=obj.last_name,
            username=obj.username,
            language_code=obj.language_code,
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
