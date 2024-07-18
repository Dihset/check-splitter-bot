from datetime import datetime

import sqlalchemy as sa
from sqlalchemy import func


class CreatedAtOnlyMixin:
    created_at = sa.Column(
        sa.DateTime(timezone=True),
        default=func.now(),
        server_default=func.now(),
        comment="Дата создания записи",
    )


class UpdatedAtMixin(CreatedAtOnlyMixin):
    updated_at = sa.Column(
        sa.DateTime(timezone=True),
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
