from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.routers.auth.schemas import AuthSchema
from api.routers.users.models import UserModel
from api.database import engine, get_db

from api.utils.authentication.password import EncryptPassword

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post('')
async def login(request: AuthSchema, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.email == request.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    if not EncryptPassword.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")

    return user
