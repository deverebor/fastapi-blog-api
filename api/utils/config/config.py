from pydantic import BaseSettings


class Configuration(BaseSettings):
    SECRET_JWT_TOKEN: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRATION_TIME: int

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
