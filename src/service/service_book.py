from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete
from sqlalchemy.future import select
from src.models.model_book import Book
from src.schemas.schema_book import BookCreate
from typing import List

async def create_book(db: AsyncSession, book: BookCreate) -> Book:
    db_book = Book(
        title = book.title,
        description = book.description,
        publication_year = book.publication_year,
        page_count = book.page_count,
        author_id = book.author,
    )
    db.add(db_book)
    await db.commit()
    await db.refresh(db_book)
    return db_book

async def get_books(db: AsyncSession, skip: int = 0, limit: int = 10) -> List[Book]:
    result = await db.execute(select(Book).offset(skip).limit(limit))
    return result.scalars().all()   

async def update_book(db: AsyncSession, book: Book):
    if book:
        db_book = await db.merge(Book, book.id)
        await db.commit()
        await db.refresh(db_book)
        return db_book
    else:
        return {"status": "error", "message": "Book not found"}

async def delete_book(db: AsyncSession, book: Book):
    result = await db.execute(select(Book).where(Book.id == book))
    author = result.scalars().first()
    if author:
        await db.execute(delete(Book).where(Book.id == book))
        await db.commit()
        return {"status": "success", "message": "Book not fount"}
    else:
        return {"status": "error", "message": "Book not found"}
