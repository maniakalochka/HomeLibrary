from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete
from sqlalchemy.future import select
from src.models.model_book import Book
from src.schemas.schema_book import BookCreate, BookUpdate
from typing import List
from fastapi import HTTPException

async def create_book(db: AsyncSession, book: BookCreate) -> Book:
    db_book = Book(
        title = book.title,
        description = book.description,
        publication_year = book.publication_year,
        page_count = book.page_count,
        author_id = book.author_id,
    )
    db.add(db_book)
    await db.commit()
    await db.refresh(db_book)
    return db_book

async def get_one_book(db: AsyncSession, book_id: int):
    result = await db.execute(select(Book).where(Book.id == book_id))
    book = result.scalars().first()
    return book

async def get_books(db: AsyncSession, skip: int = 0, limit: int = 10) -> List[Book]:
    result = await db.execute(select(Book).offset(skip).limit(limit))
    return result.scalars().all()   

async def update_book(db: AsyncSession, book_id: int, book_update: BookUpdate):
    db_book = await db.get(Book, book_id)
    if db_book:
        db_book.title = book_update.title
        db_book.author_id = book_update.author_id
        db_book.description = book_update.description
        db_book.publication_year = book_update.publication_year
        db_book.page_count = book_update.page_count

        db.add(db_book)
        await db.commit()
        await db.refresh(db_book)
        return db_book
    else:
        return HTTPException(status_code=404, detail="Author not found")

async def delete_book(db: AsyncSession, book_id: int):
    result = await db.execute(select(Book).where(Book.id == book_id))
    book = result.scalars().first()
    if book:
        await db.execute(delete(Book).where(Book.id == book_id))
        await db.commit()
        return {"status": "success", "message": "Book not fount"}
    else:
        raise HTTPException(status_code=404, detail="Book not found")
