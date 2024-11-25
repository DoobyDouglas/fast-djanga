from typing import Optional
from fastapi import FastAPI
from settings.sqldb.base import SQLBase
from settings.nosqldb.base import NoSQLBase
from hash.base import HashBase


class FastDjanga(FastAPI):
    def __init__(
        self,
        db_settings: Optional[SQLBase | NoSQLBase],
        hasher: Optional[HashBase],
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.__db_settings = db_settings
        self.__hasher = hasher
        self.__create_sessionmaker()

    @property
    def session(self):
        return self.__session_maker

    @property
    def hasher(self):
        return self.__hasher

    def __create_sessionmaker(self) -> None:
        if self.__db_settings:
            self.__session_maker = self.__db_settings._create_sessionmaker()
        else:
            self.__session_maker = None
