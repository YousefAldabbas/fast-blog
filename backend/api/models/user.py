from typing import TYPE_CHECKING

from ..config import Base

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

# A way to avoid circular imports.
if TYPE_CHECKING:
    from .item import Item  # noqa: F401

    '''
    Circular Imports is a type of Circular dependency.
    It occurs in python when two or more models import each other
    and it repeats the importing connection into an infinite circular call.
    With Circular Imports, the python script gives an error.
    '''


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True,  index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String)
    is_active = Column(Boolean(), default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    blogs = relationship("Blog", back_populates="publisher")
