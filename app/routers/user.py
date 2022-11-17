# from typing import Optional, List
# from urllib import response
# from fastapi.params import Body
# from pydantic import BaseModel
# from random import randrange
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from .. database import get_db

router = APIRouter(
    prefix= '/users',
    tags=['Users']
)

#create user
@router.post("/", status_code= status.HTTP_201_CREATED, response_model=schemas.UserOut) #title str & content str
def create_user(user: schemas.UsuerCreate, db: Session = Depends(get_db)):

    #hash the password - user.password
    # hashed_password = pwd_context.hash(user.password)
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get('/{id}', response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail= f'User with id: {id} does not exist')

    return user