from fastapi import FastAPI

from api.docs.doc import ApiInfo

from api.routers.blog import blog
from api.routers.users import users
from api.routers.auth import auth

app = FastAPI(
    title=ApiInfo.title,
    description=ApiInfo.description,
    version=ApiInfo.version,
    contact=ApiInfo.contact
)

app.include_router(blog.router)
app.include_router(users.router)
app.include_router(auth.router)
