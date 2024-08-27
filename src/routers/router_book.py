from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from typing import List

from src.schemas.schema_book import Book, BookCreate, BookUpdate
from src.db.db_config import get_db
from src.service.service_book import create_book, get_books, get_one_book, update_book, delete_book

router = APIRouter()

@router.post("/", response_model=Book)
async def create_book_endpoint(book: BookCreate, db: Session = Depends(get_db)):
    return await create_book(db=db, book=book)

@router.get("/{book_id}", response_model=Book)
async def get_one_book_endpoint(book_id: int, db: Session = Depends(get_db)):
    book = await get_one_book(db, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.get("/", response_model=List[Book])
async def get_books_endpoint(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return await get_books(db=db, skip=skip, limit=limit)

@router.put("/{book_id}", response_model=Book)
async def update_one_book(book_id: int, book_updates: BookUpdate, db: Session = Depends(get_db)):
    updated_book = await update_book(db=db, book_id=book_id, book_updates=book_updates)
    return updated_book

@router.delete("/{book_id}")
async def delete_one_book(book_id: int, db: Session = Depends(get_db)):
    return await delete_book(db=db, book_id=book_id)

