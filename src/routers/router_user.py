
from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from typing import List

from models.model_user import User as SQLAlchemyUser
from schemas.schema_user import  UserCreate, UserRead
from repository.db_config import get_db
from service.service_user import create_user, get_users

router = APIRouter()

@router.post("/", response_model=UserRead)
async def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return await create_user(db=db, user=user)

@router.get("/", response_model=List[UserRead])
async def get_users_endpoint(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return await get_users(db=db, skip=skip, limit=limit)