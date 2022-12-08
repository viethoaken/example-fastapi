# # from email import message
# from typing import Optional, List
# # from urllib import response
# from fastapi.params import Body
# from pydantic import BaseModel
# from random import randrange
from fastapi import FastAPI
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, get_db
from .routers import post, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "https://www.google.com",
    "https://www.youtube.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello world"}

# my_posts = [{'title': 'title 1', 'content': 'content 1', 'id': 1}, {'title': 'title 2', 'content': 'content 2', 'id': 2}]

# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             print('type of find post')
#             print(type(id))
#             return p

# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id']  == id:
#             return i

# @app.get('/sqlalchemy')
# def get_posts(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return {'data': posts}


    
