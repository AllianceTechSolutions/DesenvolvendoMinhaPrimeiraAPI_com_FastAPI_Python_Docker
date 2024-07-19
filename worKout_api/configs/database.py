from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore
from workout_api.configs.settings import settings # type: ignore


engine = create_async_engine(settings.DB_URL, echo=False)
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def get_session() -> AsyncGenerator:
    async with async_session() as session:
        yield session