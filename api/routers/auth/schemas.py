from pydantic import BaseModel


class AuthSchema(BaseModel):
    email: str
    password: str
