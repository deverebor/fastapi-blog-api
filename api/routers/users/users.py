from fastapi import APIRouter, Depends, Response, HTTPException, status
from sqlalchemy.orm import Session

from api.utils.authentication.password import EncryptPassword

from api.database import engine, get_db
from . import models
from .models import UserModel
from .schemas import UserSchema, ShowUserSchema

router = APIRouter()

models.Base.metadata.create_all(bind=engine)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=ShowUserSchema)
async def create(request: UserSchema, db: Session = Depends(get_db)):
    new_user = UserModel(
        first_name=request.first_name,
        last_name=request.last_name,
        email=request.email,
        password=EncryptPassword.encrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=ShowUserSchema)
async def all_users(id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user
