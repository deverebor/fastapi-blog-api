from fastapi import HTTPException, Response, status
from sqlalchemy.orm import Session

from api.routers.blog.models import BlogModel
from api.routers.blog.schemas import BlogSchema


def get_all(db: Session):
    blogs = db.query(BlogModel).all()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog not found")
    return blogs


def get_by_id(blog_id: int, db: Session):
    blog = db.query(BlogModel).filter(BlogModel.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id: {blog_id} not found")
    return blog


def create_blog(request: BlogSchema, db: Session):
    new_blog = BlogModel(title=request.title, content=request.content, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


def update_by_id(blog_id: int, request: BlogSchema, db: Session):
    blog = db.query(BlogModel).filter(BlogModel.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"success: {False}")
    blog.title = request.title
    blog.content = request.content

    db.commit()

    return Response(status_code=status.HTTP_200_OK, content=f"success: {True}")


def delete_by_id(blog_id: int, db: Session):
    blog = db.query(BlogModel).filter(BlogModel.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"success: {False}")
    db.delete(blog)
    db.commit()
    return Response(status_code=status.HTTP_200_OK, content=f"success: {True}")
