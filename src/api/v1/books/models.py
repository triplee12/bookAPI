"""Book api model for the database."""
import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import (
    UUID, TIMESTAMP
)
from sqlmodel import SQLModel, Field, Column


class Book(SQLModel, table=True):
    """Book model for the database."""
    __tablename__ = 'books'

    uid: uuid.UUID = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str
    created_at: datetime = Field(
        sa_column=Column(TIMESTAMP(timezone=True), nullable=False, default=datetime.now)
    )
    updated_at: datetime = Field(
        sa_column=Column(TIMESTAMP(timezone=True), nullable=False, default=datetime.now)
    )
    
    def __repr__(self) -> str:
        return f"<{self.title}>"
