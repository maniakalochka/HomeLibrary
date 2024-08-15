from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from typing import List

from schemas.book import Book as BookModel

router = APIRouter()



