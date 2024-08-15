
from fastapi import FastAPI
import uvicorn
from sqlalchemy.orm import Session
from typing import List

from models.books import Book as BookModel
from models.authors import Author as AuthorModel
from models.users import User as UserModel


app = FastAPI()



if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", reload=True)