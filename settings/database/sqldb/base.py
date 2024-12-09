from typing import Any, AsyncGenerator, cast
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from settings.database.base import DBase
from overrides import override
from sqlalchemy.ext.asyncio.session import async_sessionmaker
from motor.motor_asyncio import AsyncIOMotorClient


class SQLBase(DBase):
    driver: str = ""
    echo: bool = False

    def _get_kwargs(self) -> dict[str, str]:
        return {"db": self.name, "driver": self.driver, "url": self._get_url()}

    @override
    def _create_sessionmaker(
        self,
    ) -> async_sessionmaker[AsyncSession]:
        kwargs: dict[str, str | Any] = {"url": "{db}+{driver}://{url}".format(**self._get_kwargs()), "echo": self.echo}
        return async_sessionmaker(create_async_engine(**kwargs), autoflush=True, expire_on_commit=False)

    @override
    async def _get_session(
        self,
        session_maker: async_sessionmaker | AsyncIOMotorClient,
    ) -> AsyncGenerator[AsyncSession, Any]:
        session_maker_: async_sessionmaker = cast(async_sessionmaker, session_maker)
        async with session_maker_() as session:
            session_: AsyncSession = cast(AsyncSession, session)
            try:
                yield session_
            finally:
                await session_.close()


if __name__ == "__main__":
    pass
