from fastapi import APIRouter, Depends, status, HTTPException

from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy import select, insert

from src.models.model_user import User
from src.schemas.schema_user import UserCreate
from src.db.db_config import get_db
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from passlib.context import CryptContext

router = APIRouter(prefix='/auth', tags=['auth'])
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')



@router.post('/')
async def create_user(db: Annotated[AsyncSession, Depends(get_db)], create_user: UserCreate):
    await db.execute(insert(User).values(f_name=create_user.f_name,
                                         l_name=create_user.l_name,
                                         username=create_user.username,
                                         email=create_user.email,
                                         hashed_password=bcrypt_context.hash(create_user.password),
                                         ))
    await db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }


security = HTTPBasic()


async def get_current_username(db: Annotated[AsyncSession, Depends(get_db)], credentials: HTTPBasicCredentials = Depends(security)):
    user = await db.scalar(select(User).where(User.username == credentials.username))
    if not user or not bcrypt_context.verify(credentials.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return user


@router.get('/users/me')
async def read_current_user(user: str = Depends(get_current_username)):
    return {'User': user}