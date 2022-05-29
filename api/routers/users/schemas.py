from pydantic import BaseModel


class UserSchema(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str


class ShowUserSchema(BaseModel):
    first_name: str
    last_name: str
    email: str

    class Config:
        orm_mode = True
