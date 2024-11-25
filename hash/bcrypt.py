from passlib.context import CryptContext
from hash.base import HashBase
from overrides import override


class HashBcrypt(HashBase):
    def __init__(self) -> None:
        self.context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @override
    def verify(self, plain_password, hashed_password) -> bool:
        return self.context.verify(plain_password, hashed_password)

    @override
    def get(self, password) -> str:
        return self.context.hash(password)


if __name__ == "__main__":
    pass
