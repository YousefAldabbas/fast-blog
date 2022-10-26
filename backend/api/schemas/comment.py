from datetime import datetime
from time import sleep
from typing import List, Union, Optional
from pydantic import BaseModel, root_validator, EmailStr


class CommentBase(BaseModel):
    text: Optional[str] = None

    class Config:
        validate_assignment = True

    # @root_validator
    # def number_validator(cls, values):
    #     values["updated_at"] = datetime.now()
    #     return values


class CommentCreate(CommentBase):
    text: str

# Properties to receive on item update


class CommentUpdate(CommentBase):
    pass


class CommentInDBBase(BaseModel):
    text: str
    # created_at: str

    class Config():
        orm_mode = True


# Properties to return to client
class Comment(CommentInDBBase):
    pass


# Properties properties stored in DB
class CommentInDB(CommentInDBBase):
    pass
