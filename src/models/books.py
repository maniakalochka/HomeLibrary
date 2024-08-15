from pydantic import BaseModel


class Book(BaseModel):
    title: str
    description: str = ""
    publication_year: int = None
    page_count: int = None