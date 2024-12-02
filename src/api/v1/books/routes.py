from typing import Any, List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_db
# from .data import books
from .services import BookService
from .schema import CreateBookSchema, ResponseBookSchema


book_router = APIRouter(tags=["Books",])
book_service = BookService()


@book_router.get("/", response_model=List[ResponseBookSchema])
async def retrieve_books(session: AsyncSession = Depends(get_db)) -> list[dict[str, Any]]:
    """Return a list of books."""
    books = await book_service.get_all_books(session=session)
    return books


@book_router.get("/{book_id}", response_model=ResponseBookSchema)
async def get_book(book_id: str, session: AsyncSession = Depends(get_db)):
    """Return a book from the database."""
    book = await book_service.get_a_book(uid=book_id, session=session)
    if book is not None:
        return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )


@book_router.post("/create", status_code=201, response_model=ResponseBookSchema)
async def create_book(book_data: CreateBookSchema, session: AsyncSession = Depends(get_db)):
    """Create a new book"""
    try:
        book = await book_service.create_book(book_data=book_data, session=session)
        return book
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Error processing book"
        ) from e


@book_router.patch("/{book_id}/update", response_model=ResponseBookSchema)
async def update_book(book_id: str, book_data: dict, session: AsyncSession = Depends(get_db)):
    """Update a book"""
    book = await book_service.update_a_book(uid=book_id, book_data=book_data, session=session)
    if book:
        return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )


@book_router.delete("/{book_id}/delete", status_code=204)
async def delete_book(book_id: str, session: AsyncSession = Depends(get_db)):
    """Delete a book"""
    book = await book_service.delete_a_book(uid=book_id, session=session)
    if book:
        return None
    return {"error": "Book not found"}
