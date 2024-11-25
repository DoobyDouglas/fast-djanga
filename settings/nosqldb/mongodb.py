from motor.motor_asyncio import AsyncIOMotorClient
from settings.nosqldb.base import NoSQLBase
from overrides import override


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


if __name__ == "__main__":
    pass
