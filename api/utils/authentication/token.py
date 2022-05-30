from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import HTTPException

from api.routers.auth.models import TokenData
from api.utils.config.config import Configuration

config = Configuration()


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config.SECRET_JWT_TOKEN, algorithm=config.ALGORITHM)
    return encoded_jwt


def verify_jwt_token(token: str, credentials_exception: HTTPException):
    try:
        payload = jwt.decode(token, config.SECRET_JWT_TOKEN, algorithms=[config.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception

    return token_data
