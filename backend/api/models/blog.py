from typing import TYPE_CHECKING

from ..config import Base

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

if TYPE_CHECKING:
    from .user import User


class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    user_id = Column(Integer, ForeignKey('users.id'))
    comments = relationship("Comment", back_populates="blog")
    publisher = relationship("User", back_populates="blogs")
