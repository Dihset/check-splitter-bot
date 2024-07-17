from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


class Database:
    def __init__(self, url: str, ro_url: str) -> None:
        self._async_engine = create_async_engine(
            url=url,
            pool_pre_ping=True,
            # echo=settings.ECHO_SQL,
            isolation_level="READ COMMITTED",
        )
        self._async_session = async_sessionmaker(
            bind=self._async_engine,
            expire_on_commit=False,
        )

        self._read_only_async_engine = create_async_engine(
            url=ro_url,
            pool_pre_ping=True,
            # echo=settings.ECHO_SQL,
            isolation_level="AUTOCOMMIT",
        )
        self._read_only_async_session = async_sessionmaker(
            bind=self._read_only_async_engine,
            expire_on_commit=False,
        )

    @asynccontextmanager
    async def get_session(self) -> AsyncGenerator[AsyncSession, Any]:
        session: AsyncSession = self._async_session()
        try:
            yield session
        except SQLAlchemyError:
            await session.rollback()
            raise
        finally:
            await session.commit()
            await session.close()

    @asynccontextmanager
    async def get_read_only_session(self) -> AsyncGenerator[AsyncSession, Any]:
        session: AsyncSession = self._read_only_async_session()
        try:
            yield session
        except SQLAlchemyError:
            raise
        finally:
            await session.close()
