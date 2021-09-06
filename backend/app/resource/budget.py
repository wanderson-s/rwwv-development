# INPUT
from starlette import status
from app.common.response import BAD_REQUEST_400
from app.config.settings import settings
from app.model.database import get_db
from app.schema.input.budget import BaseBudget

# OUTPUT
from app.schema.output.budget import (
    BaseModelBudget,
    BaseModelBudgetEmployee,
    BaseModelBudgetsEmployee,
)

from app.controller import budget
from fastapi import APIRouter, Depends, FastAPI, Query
from sqlalchemy.orm.session import Session


def init_app(app: FastAPI):
    router = APIRouter()

    @router.post(
        "/budget",
        response_model=BaseModelBudget,
        responses=BAD_REQUEST_400,
        status_code=status.HTTP_201_CREATED,
    )
    async def post_budget(bud: BaseBudget, db: Session = Depends(get_db)):
        return budget.insert_budget(bud=bud, db=db)

    @router.get("/budget", response_model=BaseModelBudgetsEmployee)
    async def get_budget_by_employee_id(
        employee_id: int = Query(...), db: Session = Depends(get_db)
    ):
        return budget.select_budgets_by_employee_id(employee_id=employee_id, db=db)

    @router.get("/budget/{budget_id}", response_model=BaseModelBudgetEmployee)
    async def get_budget_by_budget_id(budget_id: int, db: Session = Depends(get_db)):
        return budget.select_budget_by_budget_id(budget_id=budget_id, db=db)

    @router.delete(
        "/budget/{budget_id}",
        response_model=BaseModelBudgetEmployee,
        responses=BAD_REQUEST_400,
    )
    async def delete_budget_by_budget_id(budget_id: int, db: Session = Depends(get_db)):
        return budget.delete_budget_by_id(budget_id=budget_id, db=db)

    @router.patch(
        "/budget/{budget_id}",
        response_model=BaseModelBudgetEmployee,
        responses=BAD_REQUEST_400,
    )
    async def patch_budget_by_budget_id(
        budget_id: int, bud: BaseBudget, db: Session = Depends(get_db)
    ):
        return budget.update_budget_by_id(budget_id=budget_id, bud=bud, db=db)

    app.include_router(router=router, prefix=settings.api_v1, tags=["Budget"])
