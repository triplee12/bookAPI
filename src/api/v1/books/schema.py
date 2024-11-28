from typing import Optional
from pydantic import BaseModel


class CreateBookSchema(BaseModel):
    """Create book schema"""
    id: Optional[int] = 0
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


class UpdateBookSchema(BaseModel):
    """Update book schema"""
    title: Optional[str] = ""
    author: Optional[str] = ""
    publisher: Optional[str] = ""
    published_date: Optional[str] = ""
    page_count: Optional[int] = 0
    language: Optional[str] = ""
