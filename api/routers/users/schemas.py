from pydantic import BaseModel


class UserSchema(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
