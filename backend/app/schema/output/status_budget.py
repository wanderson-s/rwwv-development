from datetime import datetime
from pydantic import validator
from app.schema.input.status_budget import BaseStatusBudget
from app.schema.input.common.budget import BaseModelBudget


class BaseModelStatusBudgetDefault(BaseStatusBudget):
    id: int
    created_at: datetime
    updated_at: datetime

    @validator("created_at", "updated_at")
    def validade_datetime(cls, v):
        return f"{v}"

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class BaseModelStatusBudget(BaseModelStatusBudgetDefault):
    budget: BaseModelBudget
    # business:...
