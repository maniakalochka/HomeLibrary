from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from models.model_author import Author 
from sqlalchemy.future import select
from schemas.schema_author import AuthorCreate

async def create_author(db: AsyncSession, author: AuthorCreate):
    db_author = Author(
        fullname = author.fullname
    )
    db.add(db_author)
    await db.commit()
    await db.refresh(db_author)
    return db_author

async def get_authors(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Author).offset(skip).limit(limit))
    return result.scalars().all()