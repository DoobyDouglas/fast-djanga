from overrides import override
from settings.broker.base import BrokerBase


class RabbitMQSettings(BrokerBase):
    RABBITMQ_DEFAULT_USER: str
    RABBITMQ_DEFAULT_PASS: str
    RABBITMQ_HOST: str
    RABBITMQ_PORT: int
    RABBITMQ_DEFAULT_VHOST: str
    RABBITMQ_BACKEND: str

    @override
    def _get_url(self) -> str:
        return (
            f"amqp://{self.RABBITMQ_DEFAULT_USER}:"
            f"{self.RABBITMQ_DEFAULT_PASS}@"
            f"{self.RABBITMQ_HOST}:{self.RABBITMQ_PORT}"
        )

    def get_broker(self) -> str:
        return (
            f"{self._get_url()}/{self.RABBITMQ_DEFAULT_VHOST}"
        )

    def get_backend(self) -> str:
        return self.RABBITMQ_BACKEND


rabbitmq_ = RabbitMQSettings()


if __name__ == "__main__":
    pass
