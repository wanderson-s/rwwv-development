from datetime import datetime
from pydantic import BaseModel
from app.model.tables import EmploymentType


class ModelPosition(BaseModel):
    id: int
    name: str
    employment_type: EmploymentType
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


# resource > controller > model > controller > resource

# schema ->  resource
