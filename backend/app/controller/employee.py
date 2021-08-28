from hashlib import md5
from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status
from app.model.tables import Employee

# INPUT
from app.schema.input.employee import BaseEmployee

# OUTPUT
from app.schema.output.employee import BaseModelEmployee


def insert_employee(empl: BaseEmployee, db: Session) -> BaseModelEmployee:
    if select_employee_by_email(email=empl.email, db=db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists."
        )
    empl.password = md5(empl.password.encode()).hexdigest()
    employee = Employee(**empl.dict())
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee


def select_employee_by_id(id: int, db: Session) -> BaseModelEmployee:
    return db.query(Employee).filter(Employee.id == id).first()


def select_employee_by_email(email: str, db: Session) -> BaseModelEmployee:
    return db.query(Employee).filter(Employee.email == email).first()
