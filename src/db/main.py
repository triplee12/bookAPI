"""Database connection module."""
from sqlmodel import create_engine, text, SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import sessionmaker
from src.config import settings
from src.api.v1.books.models import Book

PASSWORD = settings.PASSWORD
DB_NAME = settings.DB_NAME
DB_USER = settings.DB_USER
SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{PASSWORD}@localhost:5432/{DB_NAME}"

async_engine = AsyncEngine(
    create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
)


async def init_db():
    """Initialize the database."""
    async with async_engine.begin() as conn:
        extension = text("CREATE EXTENSION IF NOT EXISTS pgcrypto")
        await conn.execute(extension)
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_db():# -> Generator[Any, Any, None]
    """Get database session"""
    Session = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

    async with Session() as session:
        yield session
