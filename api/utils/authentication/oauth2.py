from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from api.utils.config.config import Configuration
from .token import verify_jwt_token

config = Configuration()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth")


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    verify_jwt_token(token, credentials_exception)
