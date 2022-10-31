from ..schemas.user import UserCreate, UserUpdate
from ..models.user import User
from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, models
from ..config import get_db
from sqlalchemy.orm import Session
from ..controllers import user
from .. import security

router = APIRouter(
    prefix='/user',
    tags=['users']
)


@router.post('/', response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(req: schemas.user.UserCreate, db: Session = Depends(get_db)):
    return user.create(req, db)


@router.get('/me', response_model=schemas.user.User)
def show_me(current_user=Depends(security.get_current_user)):
    return current_user


# show current user information
# https://sqlmodel.tiangolo.com/tutorial/fastapi/update/
@router.patch('/me', response_model=schemas.user.User)
def update_info(req: UserUpdate, db: Session = Depends(get_db), current_user=Depends(security.get_current_user)):
    return user.update(req,current_user,db)

@router.delete('/',response_model=schemas.user.User)
def delete_me(db: Session = Depends(get_db), current_user = Depends(security.get_current_user)):
    return user.delete(current_user.id,db)

# @router.get('/{id}', response_model=schemas.user.TestUserInDB)
# def show_user(id: int, db: Session = Depends(get_db)):
#     return user.show(id, db)
