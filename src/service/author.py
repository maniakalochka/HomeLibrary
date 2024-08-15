from sqlalchemy.orm import Session
from models.author import Author as AuthorModel
from schemas.author import AuthorCreate

def create_book(db: Session, author: AuthorCreate):
    db_author = AuthorModel(**author.model_dump())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_authors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(AuthorModel).offset(skip).limit(limit).all()