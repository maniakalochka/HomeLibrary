import uvicorn  # Веб-вервер для Python
import asyncio 
import json
from auth.manager import auth_backend, current_active_user
from db.db_config import init_db
from fastapi import FastAPI, Depends

from models.model_user import User 
from fastapi_users import fastapi_users, FastAPIUsers
from db.db_config import init_db
from auth.manager import get_user_manager

from schemas.schema_user import UserCreate, UserRead, UserUpdate
from routers import router_author, router_book, router_user
from auth.manager import fastapi_users


app = FastAPI()

# with open("/home/maniakalochka/openapi.json") as f:
#     custom_openapi = json.load(f)

# app.openapi_schema = custom_openapi

fastapi_users = FastAPIUsers[User, int](  
    get_user_manager,
    [auth_backend],
)  # Модель пользователя, позволяет создавать, обновлять, удалять и искать пользователей


# подключение маршрутизаторов к приложению, управляют юзерами и auth
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)
# маршрутизация для авторов и книг
app.include_router(router_author.router, prefix="/authors", tags=["authors"]) 
app.include_router(router_book.router, prefix="/books", tags=["books"])

@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    """Защищенный маршрут для GET"""
    return {"message": f"Hello {user.email}!"}


@app.on_event("startup")  # функция on_startup вызывает функции для события
async def on_startup():
    await init_db()

if __name__ == "__main__":
    asyncio.run(init_db)
    uvicorn.run("main:app", host="localhost", reload=True)