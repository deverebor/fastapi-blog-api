from passlib.context import CryptContext


class EncryptPassword:
    def encrypt(self: str):
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        hashed_password = pwd_context.hash(self)
        return hashed_password
