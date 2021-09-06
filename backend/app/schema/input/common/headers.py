from app.model.enum import EnumEmploymentType
from pydantic import BaseModel


class BaseUser(BaseModel):
    id: int
    sub: str
    first_name: str
    last_name: str
    position: EnumEmploymentType


class BaseRole(BaseModel):
    is_admin: bool
    active: bool
    can_simulate_budget: bool
    can_submit_budget: bool
    can_approve_budget: bool
    can_read_budget: bool


class BaseAuthorization(BaseModel):
    user: BaseUser
    role: BaseRole
    exp: int
