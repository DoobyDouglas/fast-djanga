from typing import Any, AsyncGenerator, Optional
from settings.base import Base
from sqlalchemy.ext.asyncio.session import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from motor.motor_asyncio import AsyncIOMotorClient


class DBase(Base):
    name: str = ""

    async def _get_session(
        self, session_maker: async_sessionmaker | AsyncIOMotorClient
    ) -> AsyncGenerator[Optional[AsyncSession | AsyncIOMotorClient], Any]:
        yield None
        raise NotImplementedError

    def _get_url(self) -> str:
        raise NotImplementedError

    def _create_sessionmaker(
        self,
    ) -> AsyncIOMotorClient | async_sessionmaker:
        raise NotImplementedError
