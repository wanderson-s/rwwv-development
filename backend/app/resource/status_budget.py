from fastapi import APIRouter
from fastapi import Depends
from fastapi import FastAPI
from fastapi import Query
from fastapi import status
from sqlalchemy.orm.session import Session

from app.config.settings import settings
from app.model.database import get_db
from app.controller import status_budget

# INPUT
from app.schema.input.status_budget import BaseStatusBudget

# OUTPUT
from app.schema.output.status_budget import BaseModelStatusBudget


def init_app(app: FastAPI):
    router = APIRouter()

    @router.post("/status_budget", response_model=BaseModelStatusBudget)
    async def post_status_budget(
        status_bud: BaseStatusBudget, db: Session = Depends(get_db)
    ):
        return status_budget.insert_status_budget(status_bud=status_bud, db=db)

    app.include_router(router=router, prefix=settings.api_v1, tags=["Status Budget"])
