from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.model_book import Book
from schemas.schema_book import BookCreate
from typing import List

async def create_book(db: AsyncSession, book: BookCreate) -> Book:
    db_book = Book(**book.model_dump())
    db.add(db_book)
    await db.commit()
    await db.refresh(db_book)
    return db_book

async def get_books(db: AsyncSession, skip: int = 0, limit: int = 10) -> List[Book]:
    result = await db.execute(select(Book).offset(skip).limit(limit))
    return result.scalars().all()   