import io
from pathlib import Path

from alembic.config import Config as AlembicConfig


def get_test_alembic_config(url: str) -> None:
    """Применение миграций к тестовой БД."""

    base_dir = Path(__file__).parent.parent.parent
    alembic_ini = base_dir / "alembic.ini"

    stdout = io.StringIO("")
    alembic_config = AlembicConfig(str(alembic_ini), stdout=stdout)

    alembic_config.set_main_option("sqlalchemy.url", url)

    return alembic_config
