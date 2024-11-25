from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, AsyncGenerator
from fastapi import Request


async def get_session(
    request: Request,
) -> AsyncGenerator[Any, Any]:
    if request.app._session is not None:
        async with request.app._session() as session:
            session: AsyncSession
            try:
                yield session
            finally:
                await session.close()
    else:
        yield


if __name__ == "__main__":
    pass
