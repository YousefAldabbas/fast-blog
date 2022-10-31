from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from .. import models, security
from ..schemas import Blog, Comment
from ..schemas import blog
from .. import schemas
from ..controllers import blog, comment
from sqlalchemy.orm import Session
from .comment import router as comment_router
from ..config import get_db


router = APIRouter(
    prefix='/blogs',
    tags=['blogs'],

)


@router.get('/', response_model=List[Blog])
def all(db: Session = Depends(get_db)) -> dict:
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED,)
async def create(req: schemas.blog.BlogCreate, db: Session = Depends(get_db), current_user=Depends(security.get_current_user)) -> dict:
    return blog.create(req, db, current_user.id)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(id: int, db: Session = Depends(get_db), current_user=Depends(security.get_current_user)):
    return blog.delete(id, db)


@router.patch('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update(id: int, req: schemas.blog.BlogCreate, db: Session = Depends(get_db), current_user=Depends(security.get_current_user)) -> dict:
    return blog.update(id, req, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=Blog)
def show(id: int, db: Session = Depends(get_db)) -> dict:
    return blog.get_one(id, db)
