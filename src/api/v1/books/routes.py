from typing import Any
from fastapi import APIRouter
from .data import books
from .schema import CreateBookSchema

book_router = APIRouter(tags=["Books",])


@book_router.get("/")
async def retrieve_books() -> list[dict[str, Any]]:
    """Return a list of books."""
    return books


@book_router.get("/{book_id}")
async def get_book(book_id: int):
    """Return a book from the database."""
    for book in books:
        if book["id"] == book_id:
            return book
    return {"error": "Book not found"}


@book_router.post("/create", status_code=201)
async def create_book(book: CreateBookSchema):
    """Create a new book"""
    _id = len(books) + 1
    book.id = _id
    books.append(book.__dict__)
    return {"message": "Book created successfully"}


@book_router.patch("/{book_id}/update")
async def update_book(book_id: int, book_data: dict):
    """Update a book"""
    for book in books:
        if book["id"] == book_id:
            book.update(book_data)
            return book
    return {"error": "Book not found"}


@book_router.delete("/{book_id}/delete", status_code=204)
async def delete_book(book_id: int):
    """Delete a book"""
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return None
    return {"error": "Book not found"}
