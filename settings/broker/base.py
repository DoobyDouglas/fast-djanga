from settings.base import Base


class BrokerBase(Base):
    def _get_url(self) -> str:
        raise NotImplementedError


if __name__ == "__main__":
    pass
