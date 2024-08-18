
from fastapi import FastAPI

# from schemas.schema_book import Book 
# from schemas.schema_author import Author 
# from schemas.schema_user import User 
from routers import router_author, router_book, router_user



app = FastAPI()
app.include_router(router_user.router, prefix="/users", tags=["users"])
app.include_router(router_author.router, prefix="/authors", tags=["authors"])
app.include_router(router_book.router, prefix="/books", tags=["books"])