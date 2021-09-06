from sqlalchemy.orm import Session
from fastapi import HTTPException
from starlette import status
from app.model.tables import BusinessUnit
from app.model.tables import Employee

# INPUT
from app.schema.input.bu import BaseBu, BaseBuToUpdate

# OUTPUT
from app.schema.output.bu import BaseModelBu, BaseModelBus


def insert_bu(buss_u: BaseBu, db: Session) -> BaseModelBu:
    bu = BusinessUnit(**buss_u.dict())
    db.add(bu)
    db.commit()
    db.refresh(bu)
    return bu


def select_bu(id: int, db: Session) -> BaseModelBu:
    return db.query(BusinessUnit).filter(BusinessUnit.id == id).first()


def select_bu_by_employee_id(employee_id: int, db: Session) -> BaseModelBus:
    data = db.query(Employee).filter(Employee.id == employee_id).scalar()
    return data


def update_bu(id: int, buss_u: BaseBuToUpdate, db: Session) -> BaseModelBu:
    bu = select_bu(id=id, db=db)
    if not bu:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Id does not exists.")
    row = buss_u.dict(exclude_none=True)
    if not row:
        raise HTTPException(
            status_code=status.HTTP_206_PARTIAL_CONTENT, detail="No data to change."
        )
    db.query(BusinessUnit).filter(BusinessUnit.id == id).update(row, synchronize_session=False)
    db.commit()
    db.refresh(bu)
    return bu


def delete_bu(id: int, db: Session) -> BaseModelBu:
    if not select_bu(id=id, db=db):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Id does not exists.")
    bu = db.query(BusinessUnit).filter(BusinessUnit.id == id).first()
    db.delete(bu)
    db.commit()
    return bu
