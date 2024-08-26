from fastapi_users import schemas

from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)
    f_name: str = Field(..., min_length=1, max_length=50)
    l_name: str = Field(..., min_length=1, max_length=50)
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
class UserRead(schemas.BaseUser[int]):
    id: int
    email: EmailStr
    f_name: str
    l_name: str
    is_active: bool
    is_superuser: bool
    is_verified: bool
    class Config:
        from_attributes = True


class UserUpdate(schemas.BaseUserUpdate):
    email: EmailStr
    f_name: str
    l_name: str
    is_active: bool
    is_superuser: bool
    is_verified: bool
