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


@router.post('/{id}/comments/')
def add_comment(id: int, req: CommentCreate, db: Session = Depends(get_db), current_user=Depends(security.get_current_user)):
    return comment.add(id, req, db, current_user.id)


@router.patch('/{id}/comments/{comment_id}')
def update_comment(id: int, comment_id: int, req: CommentCreate, db: Session = Depends(get_db), current_user=Depends(security.get_current_user)):
    return comment.update(comment_id, req, db, current_user.id)


@router.delete('/{id}/comments/{comment_id}')
def delete_comment(id: int, comment_id: int, db: Session = Depends(get_db), current_user=Depends(security.get_current_user)):
    return comment.delete(comment_id, db, current_user.id)
