from pydantic import BaseModel
from pydantic.fields import Field


class BaseBudget(BaseModel):
    name: str = Field(..., max_length=100)
    fk_id_employees: int = Field(..., alias="employee_id")
