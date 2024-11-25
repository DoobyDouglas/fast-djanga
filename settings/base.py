from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import os


load_dotenv()


class Base(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=os.getenv("ENV_FILE"),
        extra="ignore",
        alias_generator=lambda i: i.lower(),
    )


if __name__ == "__main__":
    pass
