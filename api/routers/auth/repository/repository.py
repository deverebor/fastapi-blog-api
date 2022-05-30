from datetime import timedelta

from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from api.routers.users.models import UserModel
from api.utils.authentication.token import create_access_token

from api.utils.authentication.password import EncryptPassword
from api.utils.config.config import Configuration


config = Configuration()


def login_user(request: OAuth2PasswordRequestForm, db: Session):
    user = db.query(UserModel).filter(UserModel.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    if not EncryptPassword.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")

    access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRATION_TIME)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
