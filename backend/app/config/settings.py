from os import getenv as _ge
from pydantic import BaseSettings as _BS


class _Settings(_BS):
    database_uri: str = _ge("DATABASE_URI")
    jwt_secret: str = _ge("JWT_SECRET")
    jwt_regex: str = r"(^[A-Za-z0-9-=]+\.[A-Za-z0-9-=]+\.?[A-Za-z0-9-_.+\/=]*$)|(^[B-b]earer\s[A-Za-z0-9-=]+\.[A-Za-z0-9-=]+\.?[A-Za-z0-9-_.+\/=]*$)"
    api_v1: str = "/v1"
    origins: list = ["*"]


settings = _Settings()
