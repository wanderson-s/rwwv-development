from hashlib import md5
from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status
from app.model.tables import Employee

# INPUT
from app.schema.input.employee import BaseEmployee, BaseEmployeeToUpdate

# OUTPUT
from app.schema.output.employee import BaseModelEmployee


def insert_employee(empl: BaseEmployee, db: Session) -> BaseModelEmployee:
    if select_employee_by_email(email=empl.email, db=db, ilike=False):
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
    data = db.query(Employee).filter(Employee.id == id).first()
    return data


def select_employee_by_email(
    email: str, db: Session, ilike: bool = True
) -> BaseModelEmployee:
    if ilike:
        return db.query(Employee).filter(Employee.email.ilike((f"%{email}%"))).first()
    return db.query(Employee).filter(Employee.email == email).first()


def update_employee(
    id: int, empl: BaseEmployeeToUpdate, db: Session
) -> BaseModelEmployee:
    user = select_employee_by_id(id=id, db=db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Id does not exists."
        )
    if empl.password:
        empl.password = md5(empl.password.encode()).hexdigest()
    row = empl.dict(exclude_none=True)
    if not row:
        raise HTTPException(
            status_code=status.HTTP_206_PARTIAL_CONTENT, detail="No data to change."
        )
    db.query(Employee).filter(Employee.id == id).update(row, synchronize_session=False)
    db.commit()
    db.refresh(user)
    return user


def delete_employee(id: int, db: Session) -> BaseModelEmployee:
    if not select_employee_by_id(id=id, db=db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Id does not exists."
        )
    employee = db.query(Employee).filter(Employee.id == id).first()
    if employee.business:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Problem to exclude, the employee has a Business Unit.",
        )
    db.delete(employee)
    db.commit()
    return employee
