from fastapi import FastAPI

from api.routers.blog import blog
from api.routers.users import users
from api.routers.auth import auth

title = "Blog API"
description = """
    This is a simple API for a blog. It is built with FastAPI and uses SQLAlchemy for the database with SQLite.

    # Basic usage

    ## Blog endpoint

    Get: all the posts by using the `/blog` endpoint.
    Get: a specific post by using the `/blog/<int:id>` endpoint.
    Post: a new blog post by using the `/blog` endpoint.
    Put: update a specific post by using the `/blog/<int:id>` endpoint.
    Delete: delete a specific post by using the `/blog/<int:id>` endpoint.

    ## User endpoint

    Get: all the users by using the `/users` endpoint.
    Get: specific user by using the `/users/<int:id>` endpoint.
    """
version = "1.0"
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
