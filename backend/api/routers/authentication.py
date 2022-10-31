from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import schemas, models, security , serializers
from ..config import get_db

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(req: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    user = serializers.loginSerializer(req,db)
    return security.get_tokens(user.id)


@router.post('/refresh')
def refresh(current_user=Depends(security.get_current_user)):
    return security.get_tokens(current_user.id)
