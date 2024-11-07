from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, AsyncGenerator
from fastapi import Request


async def get_session(
    request: Request,
) -> AsyncGenerator[Any, Any]:
    async with request.app._session() as session:
        session: AsyncSession
        try:
            yield session
        finally:
            await session.close()


if __name__ == '__main__':
    pass
