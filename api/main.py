from fastapi import FastAPI

from api.routers.users import users
from api.routers.blog import blog

app = FastAPI()

app.include_router(blog.router, prefix="/blog", tags=["blog"])

app.include_router(users.router, prefix="/users", tags=["users"])
