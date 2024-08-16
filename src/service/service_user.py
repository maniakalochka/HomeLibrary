from sqlalchemy.orm import Session
from models.model_user import User as UserModel
from schemas.schema_user import UserCreate

def create_user(db: Session, user: UserCreate):
    db_user = UserModel(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(UserModel).offset(skip).limit(limit).all()