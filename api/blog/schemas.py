from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    content: str
