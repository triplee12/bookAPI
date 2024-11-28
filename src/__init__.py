"""Entry point for the book api."""
from fastapi import FastAPI
from src.api.v1.books.routes import book_router

VERSION = 'v1.0'

app = FastAPI(
    title="Book API",
    description="A rest API for publishing and reviewing books",
    version=VERSION
)


@app.get(f"/api/{VERSION}")
async def index() -> dict[str, str]:
    """Entry point."""
    return {"message": "Hello, world!"}

app.include_router(book_router, prefix=f"/api/{VERSION}/books")
