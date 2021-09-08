from app.schema.output.bu import BaseModelBu
from datetime import datetime
from pydantic import validator
from app.schema.input.month import BaseMonthDefault
from app.schema.output.budget import BaseModelBudgetEmployee


class BaseModelMonth(BaseMonthDefault):
    id: int
    created_at: datetime
    updated_at: datetime
    budget: BaseModelBudgetEmployee
    business: BaseModelBu

    @validator("created_at", "updated_at")
    def validade_datetime(cls, v):
        return f"{v}"

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
