from pydantic import BaseModel


class Author(BaseModel):
    fullname: str
    