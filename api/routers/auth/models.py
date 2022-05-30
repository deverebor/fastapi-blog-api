from typing import Optional

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
