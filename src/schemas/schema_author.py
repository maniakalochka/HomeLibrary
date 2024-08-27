from pydantic import BaseModel


class AuthorBase(BaseModel):
    fullname: str

class AuthorCreate(AuthorBase):
    pass
    
class Author(AuthorBase):
    id: int
    class Config:
        from_attributes = True