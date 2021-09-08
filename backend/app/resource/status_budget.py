from fastapi import APIRouter
from fastapi import Depends
from fastapi import FastAPI
from fastapi import Query
from sqlalchemy.orm.session import Session

from app.config.settings import settings
from app.model.database import get_db
from app.controller import status_budget

# INPUT
from app.schema.input.status_budget import BaseStatusBudget, BasestatusBudgetToUpdate

# OUTPUT
from app.schema.output.status_budget import BaseModelStatusBudget
from app.schema.output.budget import BaseModelBudget


def init_app(app: FastAPI):
    router = APIRouter()

    @router.post("/status_budget", response_model=BaseModelStatusBudget)
    async def post_status_budget(
        status_bud: BaseStatusBudget, db: Session = Depends(get_db)
    ):
        return status_budget.insert_status_budget(status_bud=status_bud, db=db)

    @router.get("/status_budget/{id}", response_model=BaseModelStatusBudget)
    async def get_status_budget_id(id: int, db: Session = Depends(get_db)):
        return status_budget.select_status_budget_by_id(id=id, db=db)

    @router.get("/status_budget", response_model=BaseModelBudget)
    async def get_status_budget_by_budget_id(
        budget_id: int = Query(...), db: Session = Depends(get_db)
    ):
        return status_budget.select_status_budget_by_budget_id(
            budget_id=budget_id, db=db
        )

    @router.patch("/status_budget/{id}", response_model=BaseModelStatusBudget)
    async def patch_status_budget(
        id: int, status_bud: BasestatusBudgetToUpdate, db: Session = Depends(get_db)
    ):
        return status_budget.update_status_budget(id=id, status_bud=status_bud, db=db)

    @router.delete("/status_budget/{id}", response_model=BaseModelStatusBudget)
    async def delete_status_budget(id: int, db: Session = Depends(get_db)):
        return status_budget.delete_status_budget(id=id, db=db)

    app.include_router(router=router, prefix=settings.api_v1, tags=["Status Budget"])
