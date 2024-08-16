from fastapi import FastAPI
import uvicorn # type: ignore
from sqlalchemy.orm import Session
from typing import List
import asyncio

from schemas.schema_book import Book 
from schemas.schema_author import Author 
from schemas.schema_user import User 
from routers import router_author, router_book

from db.db_config import init_db



app = FastAPI()
app.include_router(router_author.router, prefix="/authors", tags=["authors"])
app.include_router(router_book.router, prefix="/books", tags=["books"])



if __name__ == "__main__":
    asyncio.run(init_db)
    uvicorn.run("main:app", host="localhost", reload=True)