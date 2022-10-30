
from datetime import datetime
from time import sleep
from typing import List, Union, Optional
from pydantic import BaseModel, root_validator

from .user import User, Publisher, UserInDBBase
from .comment import Comment


class BlogBase(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None
    publisher: Optional[Publisher] = None
    created_at: Optional[str] = None

    class Config:
        validate_assignment = True

    # @root_validator
    # def number_validator(cls, values):
    #     values["updated_at"] = datetime.now()
    #     return values


class BlogCreate(BaseModel):
    title: str
    body: str
    # class Config():
    #     orm_mode = True

# Properties to receive on item update


class BlogUpdate(BlogBase):
    pass


class BlogInDBBase(BaseModel):
    pass


# Properties to return to client
class Blog(BlogInDBBase):
    title: str
    body: str
    publisher: Publisher
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    comments: List[Comment] = []

    class Config():
        orm_mode = True


# Properties properties stored in DB
class BlogInDB(BlogInDBBase):
    pass
