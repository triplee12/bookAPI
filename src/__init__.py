"""Entry point for the book api."""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.api.v1.books.routes import book_router
from src.db.main import init_db


@asynccontextmanager
async def life_span(app: FastAPI):
    """Application lifetime"""
    print("Server is Starting...")
    await init_db()
    yield
    print("Server has been stopped")

VERSION = 'v1.0'

app = FastAPI(
    title="Book API",
    description="A rest API for publishing and reviewing books",
    version=VERSION,
    lifespan=life_span
)


@app.get(f"/api/{VERSION}")
async def index() -> dict[str, str]:
    """Entry point."""
    return {"message": "Hello, world!"}

app.include_router(book_router, prefix=f"/api/{VERSION}/books")
