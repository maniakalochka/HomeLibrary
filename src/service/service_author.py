from sqlalchemy.orm import Session
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.model_author import Author 
from sqlalchemy.future import select
from src.models.model_book import Book
from src.schemas.schema_author import AuthorCreate, AuthorBase, AuthorUpdate
from fastapi import HTTPException

async def create_author(db: AsyncSession, author: AuthorCreate):
    db_author = Author(
        fullname = author.fullname
    )
    db.add(db_author)
    await db.commit()
    await db.refresh(db_author)
    return db_author

async def get_one_author(db: AsyncSession, author_id: int):
    result = await db.execute(select(Author).where(Author.id == author_id))
    author = result.scalars().first()
    return author


async def get_authors(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Author).offset(skip).limit(limit))
    return result.scalars().all()

async def update_author(db: AsyncSession, author_id: int, author_update: AuthorUpdate):
    db_author = await db.get(Author, author_id)
    if db_author:
        db_author.fullname = author_update.fullname
        db.add(db_author)
        await db.commit()
        await db.refresh(db_author)
        return db_author
    else:
        return HTTPException(status_code=404, detail="Author not found")

async def delete_author(db: AsyncSession, author_id: int):
    # Удаляем или обновляем связанные записи в таблице books
    await db.execute(delete(Book).where(Book.author_id == author_id))
    await db.commit()

    # Теперь можно удалить автора
    result = await db.execute(select(Author).where(Author.id == author_id))
    author = result.scalars().first()
    if author:
        await db.execute(delete(Author).where(Author.id == author_id))
        await db.commit()
        return {"status": "success", "message": "Author deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Author not found")