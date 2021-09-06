from app.schema.output.employee import BaseModelEmployee
from typing import List
from datetime import datetime
from pydantic import validator
from app.schema.input.bu import BaseBu


class BaseModelBuDefault(BaseBu):
    id: int
    created_at: datetime
    updated_at: datetime

    @validator("created_at", "updated_at")
    def validade_datetime(cls, v):
        return f"{v}"

    class Config:
        orm_mode = True


class BaseModelBu(BaseModelBuDefault):
    employee: BaseModelEmployee


class BaseModelBus(BaseModelEmployee):
    business: List[BaseModelBuDefault] = []

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
