from datetime import datetime
from pydantic import validator
from app.schema.input.bu import BaseBu


class BaseModelBu(BaseBu):
    id: int
    created_at: datetime
    updated_at: datetime

    @validator("created_at", "updated_at")
    def validade_datetime(cls, v):
        return f"{v}"

    class Config:
        orm_mode = True
