from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    nombre: str

class UserCreate(UserBase):
    password: str
    id_area: int
    id_rol: int

class UserInDB(UserBase):
    hashed_password: str
    id_area: int
    id_rol: int

class User(UserBase):
    id_usuario: int
    id_area: int
    id_rol: int

    class Config:
        orm_mode = True
