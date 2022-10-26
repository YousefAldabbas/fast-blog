from .. import models
from sqlalchemy.orm import Session
from fastapi import HTTPException, status


def add(id,req, db: Session):
    new_comment = models.Comment(text = req.text,blog_id=id, user_id=1)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)

    return new_comment
