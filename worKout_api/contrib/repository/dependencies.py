from typing import Annotated
from fastapi import  Depends # type: ignore

from sqlalchemy.ext.asyncio import AsyncSession # type: ignore

from worKout_api.configs.database import get_session

DatabaseDependency = Annotated[AsyncSession, Depends(get_session)]