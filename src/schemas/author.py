from pydantic import BaseModel


class Author(BaseModel):
    fullname: str
    
    class Config:
        orm_mode = True