from fastapi import FastAPI

from api.routers.blog import blog
from api.routers.users import users
from api.routers.auth import auth

title = "Blog API"
description = """
> This is a simple API for a blog. It is built with FastAPI and uses SQLAlchemy for the database with SQLite.

This API was made as a study project to understand how it work FastAPI and how to use.
    """
version = "1.5"
contact = {
    "name": "Lucas Souza (@deverebor)",
    "url": "https://www.oerebor.dev",
}

app = FastAPI(
    title=title,
    description=description,
    version=version,
    contact=contact
)

app.include_router(blog.router)
app.include_router(users.router)
app.include_router(auth.router)
