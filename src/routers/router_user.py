
from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from auth.manager import UserManager
from models.model_user import User as SQLAlchemyUser
from schemas.schema_user import  UserCreate, UserRead
from db.db_config import get_db
from service.service_user import create_user, get_users

router = APIRouter()

@router.post("/", response_model=UserRead)
async def create_user_endpoint(user: UserCreate, db: AsyncSession = Depends(get_db)):
    user_manager = UserManager(db)
    return user_manager.create_user(user=user)

@router.get("/", response_model=List[UserRead])
async def get_users_endpoint(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):

    user_manager = UserManager(db)
    return await user_manager.get_users(db=db, skip=skip, limit=limit)