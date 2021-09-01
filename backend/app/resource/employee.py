from fastapi import APIRouter
from fastapi import Depends
from fastapi import FastAPI
from fastapi import Query
from fastapi import status
from sqlalchemy.orm.session import Session

from app.config.settings import settings
from app.controller import employee
from app.model.database import get_db

# INPUT
from app.schema.input.employee import BaseEmployee, BaseEmployeeToUpdate

# OUTPUT
from app.schema.output.employee import BaseModelEmployee


def init_app(app: FastAPI):
    router = APIRouter()

    @router.post(
        "/employees",
        response_model=BaseModelEmployee,  # OUTPUT
        status_code=status.HTTP_201_CREATED,
    )
    async def post_employees(empl: BaseEmployee, db: Session = Depends(get_db)):  # INPUT
        return employee.insert_employee(empl=empl, db=db)

    @router.get("/employees/{id}", response_model=BaseModelEmployee)
    async def get_employees(id: int, db: Session = Depends(get_db)):
        return employee.select_employee_by_id(id=id, db=db)

    @router.get("/employees", response_model=BaseModelEmployee)
    async def get_employees_by_email(
        email: str = Query(..., regex="^[a-z0-9.]+@taimin\.com\.br"),
        db: Session = Depends(get_db),
    ):
        return employee.select_employee_by_email(email=email, db=db)

    @router.patch("/employees/{id}", response_model=BaseModelEmployee)
    async def patch_employees(
        id: int, empl: BaseEmployeeToUpdate, db: Session = Depends(get_db)
    ):
        return employee.update_employee(id=id, empl=empl, db=db)

    @router.delete("/employees/{id}", response_model=BaseModelEmployee)
    async def delete_employees(id: int, db: Session = Depends(get_db)):
        return employee.delete_employee(id=id, db=db)

    app.include_router(router=router, prefix=settings.api_v1, tags=["Employee"])
