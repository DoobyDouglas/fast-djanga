from motor.motor_asyncio import AsyncIOMotorDatabase
from settings.base import Base


class NoSQLBase(Base):
    name: str = ""

    def _get_url(self) -> str:
        raise NotImplementedError

    def get_database(
        self,
    ) -> AsyncIOMotorDatabase:
        raise NotImplementedError


if __name__ == "__main__":
    pass
