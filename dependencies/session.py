from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, AsyncGenerator
from fastapi import Request
from sqlalchemy.ext.asyncio.session import async_sessionmaker
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorClientSession


async def get_session(
    request: Request,
) -> AsyncGenerator[AsyncSession | AsyncIOMotorClientSession | None, Any]:
    db_session = request.app.session
    if not isinstance(db_session, (async_sessionmaker, AsyncIOMotorClient)):
        yield None
    elif isinstance(db_session, async_sessionmaker):
        sql_session: AsyncSession
        async with db_session() as sql_session:
            try:
                yield sql_session
            finally:
                await sql_session.close()
    elif isinstance(db_session, AsyncIOMotorClient):
        nosql_session: AsyncIOMotorClientSession
        async with await db_session.start_session() as nosql_session:
            try:
                async with nosql_session.start_transaction():
                    yield nosql_session
            finally:
                await nosql_session.end_session()


if __name__ == "__main__":
    pass
