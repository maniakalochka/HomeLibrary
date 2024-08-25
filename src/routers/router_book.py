from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from typing import List

from schemas.schema_book import Book, BookCreate
from db.db_config import get_db
from service.service_book import create_book, get_books

router = APIRouter()

@router.post("/", response_model=Book)
async def create_book_endpoint(book: BookCreate, db: Session = Depends(get_db)):
    return await create_book(db=db, book=book)

@router.get("/", response_model=List[Book])
async def get_books_endpoint(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return await get_books(db=db, skip=skip, limit=limit)

