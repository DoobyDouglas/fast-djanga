from settings.database.sqldb.base import SQLBase
from overrides import override


class PostgresSettings(SQLBase):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DB_HOST: str
    DB_PORT: int

    name: str = "postgresql"
    driver: str = "asyncpg"

    @override
    def _get_url(self) -> str:
        return f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.DB_HOST}/{self.POSTGRES_DB}"


if __name__ == "__main__":
    pass
