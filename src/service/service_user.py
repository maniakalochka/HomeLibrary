from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from models.model_user import User 
from schemas.schema_user import UserCreate

async def create_user(db: AsyncSession, user: UserCreate) -> User:
    db_user = User(
        email = user.email,
        password = user.password,
        f_name = user.f_name,
        l_name = user.l_name,
        is_active = user.is_active,
        is_superuser = user.is_superuser,
        is_verified = user.is_verified

    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def get_users(db: AsyncSession,
                     skip: int = 0,
                     limit: int = 10):
    result = await db.execute(select(User).offset(skip).limit(limit))
    return result.scalars().all()

