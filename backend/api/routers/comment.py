from fastapi import APIRouter, Depends, status, HTTPException
# from .. import schemas, database, models
# from ..controllers import blog
# from sqlalchemy.orm import Session


router = APIRouter(
    prefix='/comment',
    tags=['comment']
)


