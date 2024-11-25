from typing import Any
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from settings.base import Base


class SQLBase(Base):
    name: str = ""
    driver: str = ""
    echo: bool = False

    def _get_url(self) -> str:
        raise NotImplementedError

    def _get_kwargs(self) -> dict[str, str]:
        return {"db": self.name, "driver": self.driver, "url": self._get_url()}

    def _create_sessionmaker(
        self,
    ) -> async_sessionmaker[AsyncSession]:
        kwargs: dict[str, str | Any] = {"url": "{db}+{driver}://{url}".format(**self._get_kwargs()), "echo": self.echo}
        return async_sessionmaker(create_async_engine(**kwargs), autoflush=True, expire_on_commit=False)


if __name__ == "__main__":
    pass
