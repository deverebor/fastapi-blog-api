from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from api.database import engine, get_db
from . import models
from .schemas import UserSchema, ShowUserSchema, ShowUserWithBlogsSchema

from api.routers.users.repository import repository

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

models.Base.metadata.create_all(bind=engine)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=ShowUserSchema)
async def create(request: UserSchema, db: Session = Depends(get_db)):
    return repository.create_user(request, db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=ShowUserWithBlogsSchema)
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return repository.get_by_id(user_id, db)
