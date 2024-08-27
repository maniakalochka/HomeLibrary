
from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from models.model_user import User as SQLAlchemyUser
from schemas.schema_user import  UserCreate, UserRead
from db.db_config import get_db
from service.service_user import create_user, get_users

router = APIRouter()