from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    description: str = ""
    publication_year: int = None
    page_count: int = None

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True



