
from fastapi import FastAPI
import uvicorn # type: ignore
from sqlalchemy.orm import Session
from typing import List

from schemas.book import Book 
from schemas.author import Author 
from schemas.user import User 
from routers import book


app = FastAPI()
app.include_router(book.router, prefix="/books", tags=["books"])



if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", reload=True)