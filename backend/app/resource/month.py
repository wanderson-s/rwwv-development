from app.schema.output.budget import BaseModelBudget
from fastapi import APIRouter
from fastapi import Depends
from fastapi import FastAPI
from fastapi import Query
from fastapi import status
from sqlalchemy.orm.session import Session

from app.config.settings import settings
from app.model.database import get_db
from app.controller import month

# INPUT
from app.schema.input.month import BaseMonth, BaseMonthUpdate

# OUTPUT
from app.schema.output.month import BaseModelMonth, BaseModelMonthDefault


def init_app(app: FastAPI):
    router = APIRouter()

    @router.post("/month", response_model=BaseModelMonth)
    async def post_month(mon: BaseMonth, db: Session = Depends(get_db)):
        return month.insert_month(mon=mon, db=db)

    @router.get("/month/{id}", response_model=BaseModelMonth)
    async def get_month_by_id(id: int, db: Session = Depends(get_db)):
        return month.select_month(id=id, db=db)

    @router.get("/month", response_model=BaseModelBudget)
    async def get_month_by_budget_id(
        budget_id: int = Query(...), db: Session = Depends(get_db)
    ):
        return month.select_month_by_budget_id(budget_id=budget_id, db=db)

    @router.patch("/month", response_model=BaseModelMonth)
    async def patch_month(
        mon: BaseMonthUpdate, id: int = Query(...), db: Session = Depends(get_db)
    ):
        return month.update_month(id=id, mon=mon, db=db)

    @router.delete("/month", response_model=BaseModelMonth)
    async def delete_month(id: int = Query(...), db: Session = Depends(get_db)):
        return month.delete_month(id=id, db=db)

    app.include_router(router=router, prefix=settings.api_v1, tags=["Month"])
