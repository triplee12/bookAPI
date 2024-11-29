"""Database connection module."""
from sqlmodel import create_engine, text, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import settings
from src.api.v1.books.models import Book

PASSWORD = settings.PASSWORD
DB_NAME = settings.DB_NAME
DB_USER = settings.DB_USER
SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{PASSWORD}@localhost:5432/{DB_NAME}"

engine = AsyncEngine(
    create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
)


async def init_db():
    """Initialize the database."""
    async with engine.begin() as conn:
        extension = text("CREATE EXTENSION IF NOT EXISTS pgcrypto")
        await conn.execute(extension)
        await conn.run_sync(SQLModel.metadata.create_all)
