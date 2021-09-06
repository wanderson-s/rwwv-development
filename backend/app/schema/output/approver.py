from datetime import datetime
from pydantic import BaseModel, Field, validator
from app.schema.output.budget import BaseModelBudgetEmployee
from app.schema.output.employee import BaseModelEmployee


class BaseModelApprover(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime
    employee: BaseModelEmployee = Field(..., alias="approver")
    budget: BaseModelBudgetEmployee

    @validator("created_at", "updated_at")
    def validade_datetime(cls, v):
        return f"{v}"

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
