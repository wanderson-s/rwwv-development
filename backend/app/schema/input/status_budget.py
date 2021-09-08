from pydantic import BaseModel
from pydantic.fields import Field
from app.model.enum import EnumBudgetStatus


class BaseStatusBudget(BaseModel):
    status: EnumBudgetStatus
    current: bool = False
    fk_id_budget: int = Field(..., alias="budget_id")


class BasestatusBudgetToUpdate(BaseStatusBudget):
    status: EnumBudgetStatus = None
    current: bool = None
    fk_id_budget: int = Field(None, alias="budget_id")
