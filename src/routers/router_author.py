from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from typing import List

from src.schemas.schema_author import Author, AuthorCreate
from src.db.db_config import get_db
from src.service.service_author import create_author, get_authors, update_author, delete_author

router = APIRouter()

@router.post("/", response_model=Author)
async def create_author_endpoint(author: AuthorCreate, db: Session = Depends(get_db)):
    return await create_author(db=db, author=author)

@router.get("/{author_id}", response_model=Author)
async def get_one_author(author_id: int, db: Session = Depends(get_db)):
    author = await get_authors(db, author_id)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

@router.get("/", response_model=List[Author])
async def get_all_author(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return await get_authors(db, skip, limit)

@router.put("/{author_id}", response_model=Author)
async def update_one_author(author_id: int, db: Session = Depends(get_db)):
    return await update_author(db=db, author_id=author_id)

@router.delete("/author_id", response_model=Author)
async def delete_one_author(author_id: int, db: Session = Depends(get_db)):
    return await delete_author(db=db, author_id=author_id)