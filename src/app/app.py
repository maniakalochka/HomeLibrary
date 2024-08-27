from src.db.db_config import init_db
from fastapi import FastAPI, Depends

from src.models.model_user import User 

from src.schemas.schema_user import UserCreate, UserRead, UserUpdate


