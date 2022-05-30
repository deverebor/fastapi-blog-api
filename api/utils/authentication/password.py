from passlib.context import CryptContext


class EncryptPassword:
    def encrypt(self: str):
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        hashed_password = pwd_context.hash(self)
        return hashed_password

    @staticmethod
    def verify(hashed_password: str, plain_password: str):
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        verified_password = pwd_context.verify(plain_password, hashed_password)
        return verified_password
