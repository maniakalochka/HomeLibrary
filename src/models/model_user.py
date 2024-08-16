
from sqlalchemy import Column, Integer, String
from db.db_config import Base
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase


class User(SQLAlchemyBaseUserTable[int], Base):
    pass


