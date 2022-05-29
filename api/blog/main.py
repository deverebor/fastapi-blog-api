from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import models
from .database import engine, get_db
from .schemas import Blog

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.post("/blog")
async def create_blog(request: Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(**request.dict())
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog
