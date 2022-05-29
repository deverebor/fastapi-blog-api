from typing import List

from fastapi import APIRouter, Depends, Response, HTTPException, status
from sqlalchemy.orm import Session

from api.database import engine, get_db

from api.routers.blog.repository import repository

from . import models
from .models import BlogModel
from .schemas import BlogSchema, ShowBlogSchema

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)

models.Base.metadata.create_all(bind=engine)


@router.get("", status_code=status.HTTP_200_OK, response_model=List[ShowBlogSchema])
async def get_all_blogs(db: Session = Depends(get_db)):
    return repository.get_all(db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=ShowBlogSchema)
async def get_single_blog(id: int, db: Session = Depends(get_db)):
    return repository.get_by_id(id, db)


@router.post("", status_code=status.HTTP_201_CREATED)
async def create(request: BlogSchema, db: Session = Depends(get_db)):
    return repository.create_blog(request, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update(id: int, request: BlogSchema, db: Session = Depends(get_db)):
    return repository.update_by_id(id, request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def destroy(id: int, db: Session = Depends(get_db)):
    return repository.delete_by_id(id, db)
