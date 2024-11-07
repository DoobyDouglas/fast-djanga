from settings.cache.base import CacheBase


class RedisSettings(CacheBase):
    REDIS_USERNAME: str
    REDIS_PASSWORD: str
    REDIS_HOST: str
    REDIS_PORT: int

    broker_index: int = 0
    backend_index: int = 1
    cache_index: int = 2

    def _get_url(self) -> str:
        return f"redis://:{self.REDIS_PASSWORD}@" f"{self.REDIS_HOST}:{self.REDIS_PORT}"

    def get_kwargs(self) -> dict:
        return {
            "username": self.REDIS_USERNAME,
            "password": self.REDIS_PASSWORD,
            "host": self.REDIS_HOST,
            "port": self.REDIS_PORT,
            "db": self.cache_index,
            "decode_responses": True,
        }

    def get_backend(self) -> str:
        return f"{self._get_url()}/{self.backend_index}"

    def get_broker(self) -> str:
        return f"{self._get_url()}/{self.broker_index}"


if __name__ == "__main__":
    pass
