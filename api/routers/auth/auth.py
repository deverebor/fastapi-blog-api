from datetime import timedelta
from functools import lru_cache

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.routers.auth.schemas import AuthSchema
from api.routers.users.models import UserModel
from api.database import engine, get_db

from .token import create_access_token

from api.utils.authentication.password import EncryptPassword
from api.utils.config.config import Configuration

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

config = Configuration()


@router.post('')
async def login(request: AuthSchema, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.email == request.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    if not EncryptPassword.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")

    access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRATION_TIME)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
