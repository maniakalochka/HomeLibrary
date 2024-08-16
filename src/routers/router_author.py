from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from typing import List

from schemas.schema_author import Author, AuthorCreate
from db.db_config import get_db
from service.service_author import create_author, get_authors

router = APIRouter()

@router.post("/", response_model=Author)
async def create_book_endpoint(author: AuthorCreate, db: Session = Depends(get_db)):
    return await create_author(db=db, author=author)

@router.get("/", response_model=List[Author])
async def get_books_endpoint(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return await get_authors(db=db, skip=skip, limit=limit)


