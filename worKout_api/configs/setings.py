from pydantic import Field, BaseSettings # type: ignore
from pydantic_settings import BaseSettings # type: ignore

class Settings(BaseSettings):
    DB_URL: str = Field(default='postegresql+asyncpg://workout@localhost/workout')

settings = Settings()

