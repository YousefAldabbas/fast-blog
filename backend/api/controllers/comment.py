from .. import models
from sqlalchemy.orm import Session
from fastapi import HTTPException, status


def add(id, req, db: Session, user_id):
    new_comment = models.Comment(text=req.text, blog_id=id, user_id=int(user_id))
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


def update(id, req, db: Session,user_id):
    comment = db.query(models.Comment).filter(
        models.Comment.id == id).first()

    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    if comment.user_id != user_id:
        raise HTTPException(
            status_code=401, detail="User doesn't have the permission to delete another user comment")
    comment_data = req.dict(exclude_unset=True)
    for key, value in comment_data.items():
        setattr(comment, key, value)

    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment


def delete(id: int, db: Session, user_id):
    comment = db.query(models.Comment).filter(
        models.Comment.id == id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    if comment.user_id != user_id:
        raise HTTPException(
            status_code=401, detail="User doesn't have the permission to delete another user comment")
    db.delete(comment)
    db.commit()
    return "done"
