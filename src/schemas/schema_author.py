from pydantic import BaseModel


class AuthorBase(BaseModel):
    fullname: str

class AuthorDelete(BaseModel):
    pass

class AuthorCreate(AuthorBase):
    pass

class AuthorUpdate(AuthorBase):
    pass
    
class Author(AuthorBase):
    id: int
    class Config:
        from_attributes = True