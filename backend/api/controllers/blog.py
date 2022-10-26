from .. import models
from sqlalchemy.orm import Session
from fastapi import HTTPException, status


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def get_one(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not exist")
    return blog


def create(req, db: Session, user_id):
    print(req)
    new_blog = models.Blog(title=req.title, body=req.body, user_id=int(user_id))
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    print(new_blog)

    return new_blog


def delete(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(id: int, req, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="not found")
    blog.update({"title": req.title, "body": req.body})
    db.commit()
    return "updated"