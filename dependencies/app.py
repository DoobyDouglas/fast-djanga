from fastapi import Request

from fast_djanga.app import FastDjanga


def get_app(request: Request) -> FastDjanga:
    return request.app


if __name__ == "__main__":
    pass
