from typing import Any
from settings.base import Base
from motor.motor_asyncio import AsyncIOMotorClient


class NoSQLBase(Base):
    name: str = ""

    def _get_url(self) -> str:
        raise NotImplementedError

    def _create_sessionmaker(
        self,
    ) -> AsyncIOMotorClient | Any:
        raise NotImplementedError


if __name__ == "__main__":
    pass
