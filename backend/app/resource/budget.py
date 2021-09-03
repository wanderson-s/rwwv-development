# INPUT
from app.config.settings import settings
from app.model.database import get_db
from app.schema.input.budget import BaseBudget

# OUTPUT
from app.schema.output.budget import BaseModelBudget, BaseModelBudgetEmployee

from app.controller import budget
from fastapi import APIRouter, Depends, FastAPI, Query, status
from sqlalchemy.orm.session import Session


def init_app(app: FastAPI):
    router = APIRouter()

    @router.post("/employees/{employee_id}/budget", response_model=BaseModelBudget)
    async def post_budget_by_employee_id(
        employee_id: int, bud: BaseBudget, db: Session = Depends(get_db)
    ):
        return budget.insert_budget(id=employee_id, bud=bud, db=db)

    @router.get(
        "/employees/{employee_id}/budget", response_model=BaseModelBudgetEmployee
    )
    async def get_budget_by_employee_id(employee: int):
        ...

    @router.get("/employees/{employee_id}/budget/{budget_id}")
    async def get_budget_by_id(employee: int, budget_id: int):
        ...

    app.include_router(router=router, prefix=settings.api_v1, tags=["Budget"])
