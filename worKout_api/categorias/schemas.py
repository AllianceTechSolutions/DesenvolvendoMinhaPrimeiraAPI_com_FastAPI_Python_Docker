from typing import Annotated

from pydantic import UUID4, Field # type: ignore
from workout_api.contrib.schemas import BaseSchema # type: ignore


class CategoriaIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome da categoria', example='Scale', max_length=10)]


class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description='Identificador da categoria')]
