from datetime import datetime
from app.schema.input.budget import BaseBudget


class BaseModelBudget(BaseBudget):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
