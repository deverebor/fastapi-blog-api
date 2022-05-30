from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from api.database import get_db

from .repository import repository

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post('')
async def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return repository.login_user(request, db)
