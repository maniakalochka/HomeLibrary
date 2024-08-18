from fastapi_users import schemas

class UserRead(schemas.BaseUser[int]):
    id: int
    f_name: str
    l_name: str

    class Config:
         from_attributes = True


class UserCreate(schemas.BaseUserCreate):
    f_name: str
    l_name: str

class UserUpdate(schemas.BaseUserUpdate):
    l_name: str
    f_name: str