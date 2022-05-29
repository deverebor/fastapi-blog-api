from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    content: str


class ShowBlog(Blog):
    class Config:
        orm_mode = True
