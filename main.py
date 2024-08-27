import uvicorn  # Веб-вервер для Python
import asyncio 
from fastapi import FastAPI
from src.db.db_config import init_db

app = FastAPI()

from src.routers import router_author, router_book, router_user, auth

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(router_author.router, prefix="/authors", tags=["authors"]) 
app.include_router(router_book.router, prefix="/books", tags=["books"])

@app.on_event("startup")  # функция on_startup вызывает функции для события
async def on_startup():
    await init_db()

if __name__ == "__main__":
    asyncio.run(init_db)
    uvicorn.run("main:app", host="localhost", reload=True)