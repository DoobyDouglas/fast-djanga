from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from settings.base import Base


class SQLBase(Base):
    name: str = ""
    driver: str = ""
    echo: bool = False

    def _get_url(self) -> str:
        raise NotImplementedError

    def get_kwargs(self) -> dict:
        return {"db": self.name, "driver": self.driver, "url": self._get_url()}

    def create_sessionmaker(
        self,
        echo: bool = True,
    ) -> async_sessionmaker[AsyncSession]:
        kwargs = {"url": "{db}+{driver}://{url}".format(**self.get_kwargs()), "echo": echo}
        return async_sessionmaker(create_async_engine(**kwargs), autoflush=True, expire_on_commit=False)


if __name__ == "__main__":
    pass
