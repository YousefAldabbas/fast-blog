from .. import models
from ..security import get_password_hash
from sqlalchemy.orm import Session
from fastapi import HTTPException, status


def create(req, db: Session):
    new_user = models.User(
        full_name=req.full_name, username=req.username, email=req.email, hashed_password=get_password_hash(req.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def show(id, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not exist")
    return user



def update(req,current_user, db: Session):
    db_user = db.query(models.User).filter(models.User.id == current_user.id).first()
    if not db_user:
        raise Exception("user not found")
    user_data = req.dict(exclude_unset=True)
    for key, value in user_data.items():
            setattr(db_user, key, value)
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
