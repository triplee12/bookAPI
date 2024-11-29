"""Book api service"""
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import desc, select
from .models import Book
from .schema import CreateBookSchema


class BookService:
    """Book service"""

    async def create_book(self, book_data: CreateBookSchema, session: AsyncSession):
        """Create a new book"""
        book_dict = book_data.model_dump()
        new_book = Book(**book_dict)
        session.add(new_book)
        await session.commit()
        await session.refresh(new_book)
        return new_book

    async def get_all_books(self, session: AsyncSession):
        """Retrieves all books in the database"""
        statement = select(Book).order_by(desc(Book.created_at))
        results = await session.exec(statement)
        return results.all()

    async def get_a_book(self, uid: str, session: AsyncSession):
        """Retrieves a book from the database"""
        statement = select(Book).where(Book.uid==uid)
        result = await session.exec(statement)
        book = result.first()
        return book if book is not None else None

    async def update_a_book(self, uid: str, book_data: dict, session: AsyncSession):
        """Updates a book in the database"""
        to_update = await self.get_a_book(uid, session)
        if to_update is None:
            return None
        for key, value in book_data.items():
            setattr(to_update, key, value)
        await session.commit()
        await session.refresh(to_update)
        return to_update

    async def delete_a_book(self, uid: str, session: AsyncSession):
        """Deletes a book from the database"""
        to_delete = await self.get_a_book(uid, session)
        if to_delete is None:
            return False
        await session.delete(to_delete)
        await session.commit()
        return True
