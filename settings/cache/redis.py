from overrides import override
from settings.cache.base import CacheBase


class RedisSettings(CacheBase):
    REDIS_USERNAME: str
    REDIS_PASSWORD: str
    REDIS_HOST: str
    REDIS_PORT: int

    REDIS_CACHE_INDEX: int = 2

    @override
    def _get_url(self) -> str:
        return f"redis://{self.REDIS_USERNAME}:{self.REDIS_PASSWORD}@{self.REDIS_HOST}:{self.REDIS_PORT}"

    def get_kwargs(self) -> dict:
        return {
            "username": self.REDIS_USERNAME,
            "password": self.REDIS_PASSWORD,
            "host": self.REDIS_HOST,
            "port": self.REDIS_PORT,
            "db": self.REDIS_CACHE_INDEX,
            "decode_responses": True,
        }


if __name__ == "__main__":
    pass
