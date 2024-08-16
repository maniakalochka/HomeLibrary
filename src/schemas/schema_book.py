from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    description: str = ""
    publication_year: int = 0
    page_count: int = 0

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        from_attributes = True



