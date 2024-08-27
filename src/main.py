import uvicorn  # Веб-вервер для Python
import asyncio 
import json
from db.db_config import init_db
from fastapi import FastAPI, Depends

from models.model_user import User 
from fastapi_users import fastapi_users, FastAPIUsers
from db.db_config import init_db

from schemas.schema_user import UserCreate, UserRead, UserUpdate
from routers import router_author, router_book, router_user


app = FastAPI()



app.include_router(router_author.router, prefix="/authors", tags=["authors"]) 
app.include_router(router_book.router, prefix="/books", tags=["books"])




@app.on_event("startup")  # функция on_startup вызывает функции для события
async def on_startup():
    await init_db()

if __name__ == "__main__":
    asyncio.run(init_db)
    uvicorn.run("main:app", host="localhost", reload=True)