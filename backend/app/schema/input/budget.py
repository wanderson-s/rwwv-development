from pydantic import BaseModel
from pydantic.fields import Field


class BaseBudget(BaseModel):
    name: str = Field(..., max_length=100)
