import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()  # загрузка .env

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT")

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(DATABASE_URL, echo=True)

# фабрика сессий
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession)

Base = declarative_base()  # создает базовый класс для определения моделей БД (SQLalchemy)


async def get_db():
    """получение сессии БД в асинхронном контексте."""
    async with SessionLocal() as session:
        yield session


async def init_db():
    """Асинхронная инициализация БД"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
