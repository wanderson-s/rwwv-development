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
from app.schema.input.month import BaseMonth

# OUTPUT
from app.schema.output.month import BaseModelMonth


def init_app(app: FastAPI):
    router = APIRouter()

    @router.post("/month", response_model=BaseModelMonth)
    async def post_month(mon: BaseMonth, db: Session = Depends(get_db)):
        return month.insert_month(mon=mon, db=db)

    app.include_router(router=router, prefix=settings.api_v1, tags=["Month"])
