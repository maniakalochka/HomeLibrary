from fastapi_users.db import SQLAlchemyBaseUserTable
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from db.db_config import get_db
from src.db.db_config import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True, index=True)
    f_name = Column(String, nullable=False)
    l_name = Column(String, nullable=False)
    


async def get_user_db(session: AsyncSession = Depends(get_db)):
    async with session() as session:
        yield session
