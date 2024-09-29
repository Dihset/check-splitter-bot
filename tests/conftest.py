import asyncio
from typing import Any, AsyncGenerator

import punq
import pytest
import sqlalchemy as sa
from alembic.command import downgrade, upgrade
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    create_async_engine,
)

from src.gateways.postgresql.database import Database
from src.project.configs import Settings
from src.project.configs import settings as app_settings
from src.project.containers import get_container
from tests.fixtures.database import (
    get_test_alembic_config,
)


@pytest.fixture(scope="session", autouse=True)
def settings() -> Settings:
    return app_settings


@pytest.fixture(scope="session")
def event_loop():
    """Создает инстанс евент лупа для каждого теста - нужно для БД"""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
async def async_engine(settings) -> AsyncGenerator[AsyncEngine, Any]:
    """Создает тестовую БД и проводит миграции alembic run_migrations."""

    test_db_name = settings.test_postgres_db

    assert "test_" in test_db_name, "try to create/drop production db"

    engine_for_create_db = create_async_engine(
        settings.POSTGRES_DB_URL,
        isolation_level="AUTOCOMMIT",
    )

    connection_for_create_test_db = await engine_for_create_db.connect()
    engine_with_test_db = None

    try:
        is_test_db_exists = await connection_for_create_test_db.execute(
            sa.text(f"SELECT 1 FROM pg_database WHERE datname = '{test_db_name}';"),
        )

        if not is_test_db_exists.one_or_none():
            await connection_for_create_test_db.execute(
                sa.text(f"CREATE DATABASE {test_db_name};")
            )

        engine_with_test_db = create_async_engine(
            settings.test_postgres_url,
        )

        yield engine_with_test_db

    finally:
        if engine_for_create_db:
            await engine_for_create_db.dispose()

        await connection_for_create_test_db.close()


@pytest.fixture(scope="function")
async def database(settings, async_engine):
    alembic_config = get_test_alembic_config(settings.test_postgres_url)
    async with async_engine.connect() as c:
        await c.run_sync(lambda _: upgrade(alembic_config, "head"))

    database = Database(
        url=settings.test_postgres_url,
        ro_url=settings.test_postgres_url,
    )
    yield database

    async with async_engine.connect() as c:
        await c.run_sync(lambda _: downgrade(alembic_config, "base"))


@pytest.fixture(scope="function")
async def container(settings, database):
    container = get_container()
    container.register(
        Database,
        scope=punq.Scope.singleton,
        instance=database,
    )
    return container
