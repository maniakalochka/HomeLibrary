from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

from sqlalchemy import Column, Integer, String, ForeignKey, Date, select, Boolean
from sqlalchemy.orm import relationship

from src.db.db_config import get_db
from src.db.db_config import Base


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True)
    f_name = Column(String, nullable=False)
    l_name = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)



     
async def get_user_db(session: AsyncSession = Depends(get_db)):
        yield session
