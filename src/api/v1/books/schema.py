from datetime import date, datetime
from typing import Optional
import uuid
from pydantic import BaseModel


class CreateBookSchema(BaseModel):
    """Create book schema"""
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str


class ResponseBookSchema(BaseModel):
    """Response book schema"""
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str
    created_at: datetime
    updated_at: datetime


class UpdateBookSchema(BaseModel):
    """Update book schema"""
    title: Optional[str] = ""
    author: Optional[str] = ""
    publisher: Optional[str] = ""
    published_date: Optional[str] = ""
    page_count: Optional[int] = 0
    language: Optional[str] = ""
