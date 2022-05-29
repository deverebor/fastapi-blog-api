from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from api.database import engine, get_db
from . import models
from .models import UserModel
from .schemas import UserSchema

router = APIRouter()

models.Base.metadata.create_all(bind=engine)


@router.post("", status_code=status.HTTP_201_CREATED)
async def create(request: UserSchema, db: Session = Depends(get_db)):
    new_user = UserModel(**request.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
