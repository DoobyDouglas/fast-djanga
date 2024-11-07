import jwt
from pathlib import Path
from tokens.base import TokenBase


class TokenJWT(TokenBase):
    def __init__(
        self,
        privatekey_path: str,
        publickey_path: str,
        algorithm: str = "RS256",
    ) -> None:
        self.privatekey = self.__read(privatekey_path)
        self.publickey = self.__read(publickey_path)
        self.algorithm = algorithm

    def __read(
        self,
        path: str,
    ) -> bytes:
        return Path(path).read_bytes()

    def encode(
        self,
        payload: dict,
    ) -> str:
        return jwt.encode(payload, self.privatekey, self.algorithm)

    def decode(
        self,
        token: str,
    ) -> dict:
        return jwt.decode(token, self.publickey, [self.algorithm])


if __name__ == "__main__":
    pass
