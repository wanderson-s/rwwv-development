from pydantic import BaseModel
from pydantic.fields import Field


class BaseApprover(BaseModel):
    fk_id_budget: int = Field(..., alias="id_budget")
    fk_id_approver: int = Field(..., alias="id_approver")
