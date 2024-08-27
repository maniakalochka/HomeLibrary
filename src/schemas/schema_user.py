
from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    email: EmailStr
    f_name: str     
    l_name: str
    username: str
    password: str 
    is_active: bool
    is_admin: bool

 
class UserRead(BaseModel):
    email: EmailStr
    f_name: str
    l_name: str
    is_active: bool
    is_superuser: bool
    is_verified: bool
    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    email: EmailStr
    username: str
    password: str
    f_name: str
    l_name: str
    is_active: bool
    is_admin: bool