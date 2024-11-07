from motor.motor_asyncio import AsyncIOMotorDatabase
from fastapi import Request


def get_database(
    request: Request,
) -> AsyncIOMotorDatabase:
    return request.app._database


if __name__ == '__main__':
    pass
