from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from api.database import engine, get_db

from api.routers.blog.repository import repository

from . import models
from .schemas import BlogSchema, ShowBlogSchema
from api.routers.users.schemas import UserSchema
from api.utils.authentication.oauth2 import get_current_user

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)

models.Base.metadata.create_all(bind=engine)


@router.get("", status_code=status.HTTP_200_OK, response_model=List[ShowBlogSchema])
async def get_all_blogs(db: Session = Depends(get_db), current_user: UserSchema = Depends(get_current_user)):
    return repository.get_all(db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=ShowBlogSchema)
async def get_blog_by_id(blog_id: int, db: Session = Depends(get_db), current_user: UserSchema = Depends(
    get_current_user)):
    return repository.get_by_id(blog_id, db)


@router.post("", status_code=status.HTTP_201_CREATED)
async def create(request: BlogSchema, db: Session = Depends(get_db), current_user: UserSchema = Depends(get_current_user)):
    return repository.create_blog(request, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update(blog_id: int, request: BlogSchema, db: Session = Depends(get_db), current_user: UserSchema = Depends(
    get_current_user)):
    return repository.update_by_id(blog_id, request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(blog_id: int, db: Session = Depends(get_db), current_user: UserSchema = Depends(get_current_user)):
    return repository.delete_by_id(blog_id, db)
