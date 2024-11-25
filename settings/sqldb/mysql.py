from settings.sqldb.base import SQLBase
from overrides import override


class MySQLSettings(SQLBase):
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_DATABASE: str
    MYSQL_HOST: str
    MYSQL_PORT: int

    name: str = "mysql"
    driver: str = "aiomysql"

    @override
    def _get_url(self) -> str:
        return f"{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.MYSQL_HOST}/{self.MYSQL_DATABASE}"


if __name__ == "__main__":
    pass
