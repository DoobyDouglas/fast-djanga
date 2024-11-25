from typing import Optional
from fastapi import FastAPI
from settings.sqldb.base import SQLBase
from settings.nosqldb.base import NoSQLBase
from hash.base import HashBase


class FastDjanga(FastAPI):

    def __init__(self, sql_settings: Optional[SQLBase], nosql_settings: Optional[NoSQLBase], hasher: HashBase, cruds: dict, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if sql_settings:
            self._session = sql_settings.create_sessionmaker(sql_settings.echo)
        else:
            self._session = None
        if nosql_settings:
            self._database = nosql_settings.get_database()
        else:
            self._database = None
        self.hash = hasher
        self.crud = cruds
