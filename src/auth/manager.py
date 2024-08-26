from fastapi import Depends, Request, exceptions
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
)
from schemas.schema_user import UserCreate
from typing import Optional
from sqlalchemy import select
from fastapi_users import BaseUserManager, FastAPIUsers, IntegerIDMixin, models, schemas
from sqlalchemy.ext.asyncio import AsyncSession

from models.model_user import User, get_user_db

from db.db_config import get_db

SECRET = "SECRET"  # секретный ключ o_O




async def get_user_db(session: AsyncSession = Depends(User)):
    yield SQLAlchemyUserDatabase(get_db, session)

async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)

class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    """Методы и логика для управления пользователями"""

    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


    async def get_by_email(self, email: str):
        async with self.user_db.session() as session:
            result = await session.execute(
            select(User).where(User.email == email))
        return result.scalars().first()

    async def create_user(self, user_create: UserCreate, safe: bool = True, request: Optional[Request] = None):
        existing_user = await self.get_by_email(user_create.email)
        if (existing_user is not None):
            raise exceptions.UserAlreadyExists()

        user_dict = user_create.dict()
        password = user_dict.pop("password")
        user_dict["hashed_password"] = self.password_helper.hash(password)

        created_user = User(
            email=user_dict["email"],
            hashed_password=user_dict["hashed_password"],
            f_name=user_dict["f_name"],
            l_name=user_dict["l_name"],
            is_active=user_dict["is_active"],
            is_superuser=user_dict["is_superuser"],
            is_verified=user_dict["is_verified"]
        )
        await self.user_db.create(created_user)

        await self.on_after_register(created_user, request)
        return created_user

    


    


bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)
