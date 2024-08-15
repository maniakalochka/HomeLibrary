from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from typing import List

from schemas.book import Book, BookCreate
from db.config import get_db
from service.book import create_book, get_books

router = APIRouter()

@router.post("/", response_model=Book)
def create_book_endpoint(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db=db, book=book)

@router.get("/", response_model=List[Book])
def get_books_endpoint(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_books(db=db, skip=skip, limit=limit)


