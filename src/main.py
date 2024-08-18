import uvicorn
import asyncio
from db.db_config import init_db

if __name__ == "__main__":
    asyncio.run(init_db)
    uvicorn.run("main:app", host="localhost", reload=True)