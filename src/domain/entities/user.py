from dataclasses import dataclass
from uuid import UUID


@dataclass
class User:
    telegram_id: str
    username: str
    oid: UUID | None = None
    first_name: str | None = None
    last_name: str | None = None
    language_code: str | None = None
