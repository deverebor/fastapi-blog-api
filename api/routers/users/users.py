from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from api.database import engine, get_db
from . import models
from .schemas import User

router = APIRouter()

models.Base.metadata.create_all(bind=engine)


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_user(request: User, db: Session = Depends(get_db)):
    new_user = models.User(**request.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
