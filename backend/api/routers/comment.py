from fastapi import APIRouter, Depends, status, HTTPException
from .. import models, security
from ..schemas import Blog, Comment
from ..schemas.comment import CommentCreate
from ..schemas import blog
from .. import schemas
from ..controllers import blog, comment
from sqlalchemy.orm import Session
from ..config import get_db


router = APIRouter(
    prefix='/blog',
    tags=['comment']
)



@router.post('/{id}/comment/')
def add_comment(id: int, req: CommentCreate, db: Session = Depends(get_db), current_user=Depends(security.get_current_user)):
    return comment.add(id, req, db)


@router.patch('/{id}/comment/')
def update_comment(id: int, req: Comment, db: Session = Depends(get_db), current_user=Depends(security.get_current_user)):
    return comment.update(id, req, db)


