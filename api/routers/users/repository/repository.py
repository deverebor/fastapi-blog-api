from fastapi import HTTPException, Response, status
from sqlalchemy.orm import Session

from api.routers.users.models import UserModel
from api.routers.users.schemas import UserSchema
from api.utils.authentication.password import EncryptPassword


def create_user(request: UserSchema, db: Session):
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


def get_by_id(user_id: int, db: Session):
    user = db.query(UserModel).filter(UserModel.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User ({user_id}) not found")
    return user
