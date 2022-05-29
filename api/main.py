from fastapi import FastAPI

from api.docs.doc import ApiInfo

from api.routers.users import users
from api.routers.blog import blog

app = FastAPI(
    title=ApiInfo.title,
    description=ApiInfo.description,
    version=ApiInfo.version,
    contact=ApiInfo.contact
)

app.include_router(blog.router, prefix="/blog", tags=["blog"])

app.include_router(users.router, prefix="/users", tags=["users"])
