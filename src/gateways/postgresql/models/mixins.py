from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column


class CreatedAtOnlyMixin:
    created_at: Mapped[datetime] = mapped_column(
        default=func.now(),
        server_default=func.now(),
        comment="Дата создания записи",
    )


class UpdatedAtMixin(CreatedAtOnlyMixin):
    updated_at: Mapped[datetime] = mapped_column(
        default=func.now(),
        server_default=func.now(),
        onupdate=func.now(),
        server_onupdate=func.now(),
        comment="Дата обновления записи",
    )

    @property
    def created_date(self) -> datetime:
        return self.created_at.replace(microsecond=0, tzinfo=None)

    @property
    def updated_date(self) -> datetime:
        return self.updated_at.replace(microsecond=0, tzinfo=None)
