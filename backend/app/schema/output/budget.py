from datetime import datetime
from typing import List

from pydantic.fields import Field
from app.schema.input.budget import BaseBudget
from app.schema.output.employee import BaseModelEmployee


class BaseModelBudget(BaseBudget):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class BaseModelBudgetsEmployee(BaseModelEmployee):
    budget: List[BaseModelBudget] = Field([], alias="budgets")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class BaseModelBudgetEmployee(BaseModelBudget):
    employee: BaseModelEmployee

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
