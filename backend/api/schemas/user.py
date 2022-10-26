from typing import TYPE_CHECKING
from datetime import datetime
from time import sleep
from typing import List, Union, Optional
from pydantic import BaseModel, root_validator, EmailStr

# Shared properties


class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    username: Optional[str] = None

    # class Config:
    #     validate_assignment = True

    # @root_validator
    # def number_validator(cls, values):
    #     values["updated_at"] = datetime.now()
    #     return values


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class Publisher(UserBase):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    username: Optional[str] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    is_active: Optional[bool] = True
    is_superuser: bool = False


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
