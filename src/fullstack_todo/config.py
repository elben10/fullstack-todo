from pydantic import BaseSettings


class Settings(BaseSettings):
    TITLE: str = "Fullstack Todo"


settings = Settings()
