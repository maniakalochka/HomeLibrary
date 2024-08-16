from sqlalchemy.orm import Session
from models.model_author import Author as AuthorModel
from schemas.schema_author import AuthorCreate

async def create_author(db: Session, author: AuthorCreate):
    db_author = AuthorModel(**author.model_dump())
    db.add(db_author)
    await db.commit()
    await db.refresh(db_author)
    return db_author

async def get_authors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(AuthorModel).offset(skip).limit(limit).all()