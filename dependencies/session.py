from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, AsyncGenerator
from fastapi import Request
from motor.motor_asyncio import AsyncIOMotorClient


async def get_session(
    request: Request,
) -> AsyncGenerator[AsyncSession | AsyncIOMotorClient | None, Any]:
    session_maker = request.app.session_maker
    if session_maker is None:
        yield None
    else:
        db_settings = request.app.db_settings
        session = db_settings._get_session(session_maker)
        yield await anext(session)


if __name__ == "__main__":
    pass
