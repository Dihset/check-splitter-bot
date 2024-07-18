import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from src.gateways.postgresql.models.base import BaseORM
from src.gateways.postgresql.models.mixins import UpdatedAtMixin


class UserORM(BaseORM, UpdatedAtMixin):
    __tablename__ = "user"

    oid = sa.Column(
        sa.Integer,
        primary_key=True,
        autoincrement=True,
        comment="Уникальный oid пользователя",
    )
    telegram_id: Mapped[str] = mapped_column(sa.String(12))
    first_name: Mapped[str | None] = mapped_column(sa.String(128))
    last_name: Mapped[str | None] = mapped_column(sa.String(128))
    username: Mapped[str | None] = mapped_column(sa.String(128))
    language_code: Mapped[str | None] = mapped_column(sa.String(8))
