import uvicorn  # Веб-вервер для Python
import asyncio 
from src.db.db_config import init_db
from fastapi import FastAPI, Depends
import sys
import os

from src.models.model_user import User 
from src.db.db_config import init_db


from src.schemas.schema_user import UserCreate, UserRead, UserUpdate
from src.routers import router_author, router_book, router_user, auth

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



app = FastAPI()


app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(router_author.router, prefix="/authors", tags=["authors"]) 
app.include_router(router_book.router, prefix="/books", tags=["books"])




@app.on_event("startup")  # функция on_startup вызывает функции для события
async def on_startup():
    await init_db()

if __name__ == "__main__":
    asyncio.run(init_db)
    uvicorn.run("main:app", host="localhost", reload=True)