from typing import List, Union

from app.common.headers import decode_token_is_admin
from app.common.response import BAD_REQUEST_400, PARTIAL_CONTENT_206, UNAUTHORIZED_401
from app.config.settings import settings
from app.controller import employee
from app.model.database import get_db

# INPUT
from app.schema.input.employee import BaseEmployee, BaseEmployeeToUpdate

# OUTPUT
from app.schema.output.employee import BaseModelEmployee

from fastapi import APIRouter, Depends, FastAPI, Query, status
from sqlalchemy.orm.session import Session


def init_app(app: FastAPI):
    router = APIRouter(
        responses=UNAUTHORIZED_401,  # dependencies=[Depends(decode_token_is_admin)]
    )

    @router.post(
        "/employees",
        response_model=BaseModelEmployee,
        status_code=status.HTTP_201_CREATED,
        responses=BAD_REQUEST_400,
    )
    async def post_employees(empl: BaseEmployee, db: Session = Depends(get_db)):
        return employee.insert_employee(empl=empl, db=db)

    @router.get("/employees/{id}", response_model=BaseModelEmployee)
    async def get_employees_by_id(id: int, db: Session = Depends(get_db)):
        return employee.select_employee_by_id(id=id, db=db)

    @router.get(
        "/employees", response_model=Union[List[BaseModelEmployee], BaseEmployee]
    )
    async def get_employees(
        email: str = Query(None, regex="^[a-z0-9.]+@taimin\.com\.br"),
        approver: bool = Query(False),
        db: Session = Depends(get_db),
    ):
        if approver:
            return employee.select_all_employee_approve(db=db)
        if email:
            return employee.select_employee_by_email(email=email, db=db)
        return employee.select_employee_all(db=db)

    @router.patch(
        "/employees/{id}",
        response_model=BaseModelEmployee,
        responses={**BAD_REQUEST_400, **PARTIAL_CONTENT_206},
    )
    async def patch_employees(
        id: int, empl: BaseEmployeeToUpdate, db: Session = Depends(get_db)
    ):
        return employee.update_employee(id=id, empl=empl, db=db)

    @router.delete(
        "/employees/{id}", response_model=BaseModelEmployee, responses=BAD_REQUEST_400
    )
    async def delete_employees(id: int, db: Session = Depends(get_db)):
        return employee.delete_employee(id=id, db=db)

    app.include_router(router=router, prefix=settings.api_v1, tags=["Employee"])
