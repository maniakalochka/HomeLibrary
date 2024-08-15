
from fastapi import FastAPI
import uvicorn
from sqlalchemy.orm import Session
from typing import List

from schemas.book import Book as BookModel
from schemas.author import Author as AuthorModel
from schemas.user import User as UserModel


app = FastAPI()



if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", reload=True)