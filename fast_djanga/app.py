from typing import Optional
from fastapi import FastAPI
from settings.database.sqldb.base import SQLBase
from settings.database.nosqldb.base import NoSQLBase
from hash.base import HashBase
from motor.motor_asyncio import AsyncIOMotorClient
from sqlalchemy.ext.asyncio.session import async_sessionmaker


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
    def db_settings(self):
        return self.__db_settings

    @property
    def session_maker(self):
        return self.__session_maker

    @property
    def hasher(self):
        return self.__hasher

    def __create_sessionmaker(self) -> None:
        self.__session_maker: Optional[async_sessionmaker | AsyncIOMotorClient] = None
        if self.__db_settings:
            self.__session_maker = self.__db_settings._create_sessionmaker()
