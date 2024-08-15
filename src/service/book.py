from sqlalchemy.orm import Session
from db.book import Book as BookModel
from schemas.book import BookCreate

def create_book(db: Session, book: BookCreate):
    db_book = BookModel(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(BookModel).offset(skip).limit(limit).all()