from motor.motor_asyncio import AsyncIOMotorClient
from settings.database.nosqldb.base import NoSQLBase
from overrides import override
from typing import Any, AsyncGenerator, cast
from sqlalchemy.ext.asyncio.session import async_sessionmaker


class MongoDBSettings(NoSQLBase):
    MONGO_INITDB_ROOT_USERNAME: str
    MONGO_INITDB_ROOT_PASSWORD: str
    MONGO_DB: str
    MONGO_HOST: str
    MONGO_PORT: int

    name: str = "mongodb"

    @override
    def _get_url(self) -> str:
        return (
            f"{self.name}://{self.MONGO_INITDB_ROOT_USERNAME}:"
            f"{self.MONGO_INITDB_ROOT_PASSWORD}@"
            f"{self.MONGO_HOST}:{self.MONGO_PORT}/"
        )

    @override
    def _create_sessionmaker(
        self,
        echo: bool = True,
    ) -> AsyncIOMotorClient:
        return AsyncIOMotorClient(self._get_url())

    @override
    async def _get_session(
        self,
        session_maker: async_sessionmaker | AsyncIOMotorClient,
    ) -> AsyncGenerator[AsyncIOMotorClient, Any]:
        session: AsyncIOMotorClient = cast(AsyncIOMotorClient, session_maker)
        async with await session.start_session() as transaction:
            try:
                async with transaction.start_transaction():
                    yield session
            finally:
                await transaction.end_session()


if __name__ == "__main__":
    pass
