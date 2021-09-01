from fastapi import APIRouter
from fastapi import Depends
from fastapi import FastAPI
from fastapi import Query
from fastapi import status
from sqlalchemy.orm.session import Session

from app.config.settings import settings
from app.model.database import get_db
from app.controller import bu

# INPUT

# OUTPUT
from app.schema.output.bu import BaseModelBu


def init_app(app: FastAPI):
    router = APIRouter()

    @router.get("/bu/{id}", response_model=BaseModelBu)
    async def get_bu(id: int, db: Session = Depends(get_db)):
        return bu.select_bu(id=id, db=db)

    app.include_router(router=router, prefix=settings.api_v1, tags=["Business Unit"])
