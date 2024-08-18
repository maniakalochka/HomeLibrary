
from fastapi import FastAPI, Depends

# from schemas.schema_book import Book 
# from schemas.schema_author import Author 
from schemas.schema_user import User 
from db.db_config import init_db


from schemas.schema_user import UserCreate, UserRead, UserUpdate
from routers import router_author, router_book, router_user
from app.users import auth_backend, current_active_user, fastapi_users



app = FastAPI()
app.include_router(
    fastapi_users.get_users_router(auth_backend),
    prefix="/auth/jwt", 
    tags=["auth"])

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
app.include_router(router_author.router, prefix="/authors", tags=["authors"])
app.include_router(router_book.router, prefix="/books", tags=["books"])

@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}


@app.lifespan("startup")
async def on_startup():
    await init_db()