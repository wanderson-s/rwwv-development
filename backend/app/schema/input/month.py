from pydantic.fields import Field
from app.model.enum import EnumMonthType, EnumMonths
from pydantic import BaseModel
from datetime import datetime


class BaseMonthDefault(BaseModel):
    month: EnumMonths
    year: int = Field(
        ge=datetime.now().year,
        le=datetime.now().year + 1,
        default_factory=lambda: datetime.now().year,
    )
    value: float
    type: EnumMonthType
    description: str
    comment: str


class BaseMonth(BaseMonthDefault):
    fk_id_business_unit: int = Field(..., alias="bu_id", ge=1)
    fk_id_budget: int = Field(..., alias="budget_id", ge=1)
