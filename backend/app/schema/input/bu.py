from pydantic import BaseModel, Field


class BaseBu(BaseModel):
    name: str
    product_family: str
    description: str = None
    fk_id_employees: int = Field(..., alias="employee_id")


class BaseBuToUpdate(BaseBu):
    name: str = None
    product: str = None
    description: str = None
    fk_id_employees: int = Field(None, alias="employee_id")
