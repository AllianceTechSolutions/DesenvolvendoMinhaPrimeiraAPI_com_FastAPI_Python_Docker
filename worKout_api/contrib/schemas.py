from dataclasses import Field
import datetime
from typing import Annotated
from uuid import UUID
from pydantic import BaseModel # type: ignore

class BaseSchema(BaseModel):
    class Config:
        extra = 'forbid'
        from attributes = True # type: ignore



class OutMixin(BaseSchema):
    id: Annotated[UUID, Field(description='ID do atleta')]
    created_at: Annotated[datetime, Field(description='Data de criação do atleta')]