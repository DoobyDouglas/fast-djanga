from overrides import override
from settings.broker.base import BrokerBase


class RedisSettings(BrokerBase):
    REDIS_USERNAME: str
    REDIS_PASSWORD: str
    REDIS_HOST: str
    REDIS_PORT: int

    REDIS_BROKER_INDEX: int = 0
    REDIS_BACKEND_INDEX: int = 1

    @override
    def _get_url(self) -> str:
        return f"redis://:{self.REDIS_PASSWORD}@{self.REDIS_HOST}:{self.REDIS_PORT}"

    def get_broker(self) -> str:
        return f"{self._get_url()}/{self.REDIS_BROKER_INDEX}"

    def get_backend(self) -> str:
        return f"{self._get_url()}/{self.REDIS_BACKEND_INDEX}"


if __name__ == "__main__":
    pass
