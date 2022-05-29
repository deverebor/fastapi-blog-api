from pydantic import BaseModel
from api.routers.users.schemas import ShowUserSchema


class BlogSchema(BaseModel):
    title: str
    content: str


class ShowBlogSchema(BaseModel):
    title: str
    content: str
    owner: ShowUserSchema

    class Config:
        orm_mode = True
