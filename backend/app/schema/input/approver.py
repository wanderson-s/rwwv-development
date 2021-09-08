from pydantic import BaseModel
from pydantic.fields import Field


class BaseApprover(BaseModel):
    fk_id_budget: int = Field(..., alias="budget_id")
    fk_id_approver: int = Field(..., alias="approver_id")
