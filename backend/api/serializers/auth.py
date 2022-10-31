from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import schemas, models, security
from ..config import get_db


def loginSerializer(req,db: Session):

    user = db.query(models.User).filter(
        models.User.username == req.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'invalid creadentials')

    if not security.verify_password(user.hashed_password, req.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'incorrect password')
    return user
