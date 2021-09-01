from pydantic import BaseModel


class BaseBu(BaseModel):
    name: str
    product: str
    description: str = None
    fk_id_employees: int
