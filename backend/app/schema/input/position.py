from pydantic import BaseModel
from app.model.tables import EmploymentType

class BaseModelPosition(BaseModel):
    name: str
    employment_type: EmploymentType



# resource > controller > model > controller > resource

# schema ->  resource