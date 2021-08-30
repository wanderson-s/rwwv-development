from datetime import date
from pydantic import BaseModel
from app.model.tables import EmploymentType


class BaseEmployeeNoPassword(BaseModel):
    email: str = None
    active: bool = False
    # personal
    cpf: str
    first_name: str
    last_name: str
    birth_date: date = None
    position: EmploymentType
    # permission
    can_simulate_budget: bool = False
    can_submit_budget: bool = False
    can_approve_budget: bool = False
    can_read_budget: bool = False
    is_admin: bool = False


class BaseEmployee(BaseEmployeeNoPassword):
    password: str = None

    class Config:
        orm_mode = True
