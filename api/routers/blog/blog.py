from typing import List

from fastapi import APIRouter, Depends, Response, HTTPException, status
from sqlalchemy.orm import Session

from . import models
from .models import BlogModel
from api.database import engine, get_db
from .schemas import BlogSchema, ShowBlogSchema

router = APIRouter()

models.Base.metadata.create_all(bind=engine)


@router.get("", status_code=status.HTTP_200_OK, response_model=List[ShowBlogSchema])
async def all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(BlogModel).all()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog not found")
    return blogs


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=ShowBlogSchema)
async def get_single_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(BlogModel).filter(BlogModel.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id: {id} not found")
    return blog


@router.post("", status_code=status.HTTP_201_CREATED)
async def create(request: BlogSchema, db: Session = Depends(get_db)):
    new_blog = BlogModel(**request.dict())
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update(id: int, request: BlogSchema, db: Session = Depends(get_db)):
    blog = db.query(BlogModel).filter(BlogModel.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"success: {False}")
    blog.title = request.title
    blog.content = request.content
    db.commit()
    return Response(status_code=status.HTTP_200_OK, content=f"success: {True}")


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def destroy(id: int, db: Session = Depends(get_db)):
    blog = db.query(BlogModel).filter(BlogModel.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"success: {False}")
    db.delete(blog)
    db.commit()
    return Response(status_code=status.HTTP_200_OK, content=f"success: {True}")
