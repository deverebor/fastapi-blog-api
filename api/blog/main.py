from fastapi import FastAPI

from . import models, database
from .schemas import Blog

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)


@app.post("/blog")
async def create_blog(request: Blog):
    return request
