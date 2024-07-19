from uuid import uuid4
from sqlalchemy import UUID # type: ignore
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column # type: ignore
from sqlalchemy.dialects.postgresql import UUID as PG_UUID # type: ignore

class BaseModel(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, nullable=False)