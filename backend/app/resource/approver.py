from app.common.response import BAD_REQUEST_400
from fastapi import APIRouter
from fastapi import Depends
from fastapi import FastAPI
from fastapi import Query
from fastapi import status
from sqlalchemy.orm.session import Session

from app.config.settings import settings
from app.model.database import get_db
from app.controller import approver

# INPUT
from app.schema.input.approver import BaseApprover

# OUTPUT
from app.schema.output.approver import BaseModelApprover


def init_app(app: FastAPI):
    router = APIRouter()

    @router.post(
        "/approver",
        status_code=status.HTTP_201_CREATED,
        response_model=BaseModelApprover,
        responses=BAD_REQUEST_400,
    )
    async def post_approver(appro: BaseApprover, db: Session = Depends(get_db)):
        return approver.insert_approver(appro=appro, db=db)

    @router.get("/approver/{approver_id}", response_model=BaseModelApprover)
    async def get_approver_by_id(approver_id: int, db: Session = Depends(get_db)):
        return approver.select_approver(id=approver_id, db=db)

    @router.get("/approver", response_model=BaseModelApprover)
    async def get_approver(
        employee_id: int = Query(None),
        budget_id: int = Query(None),
        db: Session = Depends(get_db),
    ):
        if employee_id:
            return approver.select_approver_by_employee_id(
                employee_id=employee_id, db=db
            )
        elif budget_id:
            return approver.select_approver_by_budget_id(budget_id=budget_id, db=db)
        return None

    @router.patch("/approver/{approver_id}", response_model=BaseModelApprover)
    async def patch_approver_by_id(
        approver_id: int, appro: BaseApprover, db: Session = Depends(get_db)
    ):
        return approver.update_approver(id=approver_id, appro=appro, db=db)

    @router.delete("/approver/{approver_id}", response_model=BaseModelApprover)
    async def delete_approver_by_id(approver_id: int, db: Session = Depends(get_db)):
        return approver.delete_approver(id=approver_id, db=db)

    app.include_router(router=router, prefix=settings.api_v1, tags=["Approver"])
