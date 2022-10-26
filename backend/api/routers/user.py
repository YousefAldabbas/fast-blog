from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, models
from ..config import get_db
from sqlalchemy.orm import Session
from ..controllers import user
router = APIRouter(
    prefix='/user',
    tags=['users']
)

# get_db = database.get_db


@router.post('/', response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(req: schemas.user.UserCreate, db: Session = Depends(get_db)):
    return user.create(req, db)


@router.get('/{id}', response_model=schemas.User)
def show_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)
