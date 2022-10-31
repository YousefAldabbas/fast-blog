import os
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from pydantic import ValidationError
from sqlalchemy.orm import Session
from . import schemas
from typing import Union, Any
from .config import get_db
from . import models
from jose import JWTError, jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/login",)

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
REFRESH_TOKEN_EXPIRE_MINUTES = int(os.getenv("REFRESH_TOKEN_EXPIRE_MINUTES"))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(
            token, SECRET_KEY, algorithms=[ALGORITHM]
        )
        if payload['scope'] != 'access_token':
            raise HTTPException(status_code=401, detail='Scope for the token is invalid')
        token_data = schemas.token.TokenData(**payload)
    except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Token expired')
    except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail='Invalid token')
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )

    user = db.query(models.User).filter(
        models.User.id == int(token_data.sub)).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user



def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta = None
) -> str:

    if expires_delta:
        expire = datetime.utcnow() + expires_delta

    else:
        expire = datetime.utcnow() + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )

    to_encode = {'scope': 'access_token',"exp": expire, "sub": str(subject)}

    encoded_jwt = jwt.encode(
        to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def create_refresh_token( subject: Union[str, Any], expires_delta: timedelta = None)-> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta

    else:
        expire = datetime.utcnow() + timedelta(
            minutes=REFRESH_TOKEN_EXPIRE_MINUTES
        )

    to_encode = {'scope': 'refresh_token',"exp": expire, "sub": str(subject)}

    encoded_jwt = jwt.encode(
        to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_password(hashed_password: str, plain_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
