class HashBase:

    def verify(self, plain_password, hashed_password) -> bool:
        raise NotImplementedError

    def get(self, password) -> str:
        raise NotImplementedError


if __name__ == '__main__':
    pass
