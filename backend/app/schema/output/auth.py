from pydantic import BaseModel


class BaseModelTokens(BaseModel):
    access_token: str
    refresh_token: str

    class Config:
        orm_mode = True
