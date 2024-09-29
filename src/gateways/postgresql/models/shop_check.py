import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from src.gateways.postgresql.models.base import BaseORM
from src.gateways.postgresql.models.mixins import UpdatedAtMixin, UUIDOidMixin


class ShopCheckORM(BaseORM, UUIDOidMixin, UpdatedAtMixin):
    __tablename__ = "shop_check"
    title: Mapped[str] = mapped_column(sa.String(128))
    creator_oid: Mapped[int] = mapped_column(sa.ForeignKey("user.oid"))


class ShopCheckItemORM(BaseORM, UUIDOidMixin, UpdatedAtMixin):
    __tablename__ = "shop_check_item"
    shop_check_oid: Mapped[int] = mapped_column(sa.ForeignKey("shop_check.oid"))
    position_title: Mapped[str] = mapped_column(sa.String(128))
    price: Mapped[float] = mapped_column(sa.Numeric(10, 2))
    count: Mapped[float] = mapped_column(sa.Numeric(10, 2))


class ShopCheckItemSplitORM(BaseORM, UUIDOidMixin, UpdatedAtMixin):
    __tablename__ = "shop_check_item_split"
    shop_check_item_oid: Mapped[int] = mapped_column(
        sa.ForeignKey("shop_check_item.oid")
    )
    user_oid: Mapped[int] = mapped_column(sa.ForeignKey("user.oid"))
    share: Mapped[int] = mapped_column(sa.Integer())
