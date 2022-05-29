from fastapi import FastAPI, Depends, Response, HTTPException, status
from sqlalchemy.orm import Session

from . import models
from .database import engine, get_db
from .schemas import Blog

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.post("/blog", status_code=status.HTTP_201_CREATED)
async def create(request: Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(**request.dict())
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


@app.get("/blog")
async def all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get("/blog/{id}", status_code=status.HTTP_200_OK)
async def get_single_blog(id: int, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id: {id} not found")
    return blog
