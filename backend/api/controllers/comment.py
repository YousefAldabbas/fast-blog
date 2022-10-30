from .. import models
from sqlalchemy.orm import Session
from fastapi import HTTPException, status


def add(id, req, db: Session):
    new_comment = models.Comment(text=req.text, blog_id=id, user_id=1)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


def update(id, req, db: Session):
    db_comment = db. db_user = db.query(models.User).filter(
        models.Comment.id == req.id).first()

    if not db_comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"comment doesn't exist")

    if db.comment.user_id != id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="un authorized",
        )
    comment_data = req.dict(exclude_unset=True)
    for key, value in comment_data.items():
        setattr(db_comment, key, value)

    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment