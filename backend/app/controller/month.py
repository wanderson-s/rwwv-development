from app.schema.output.budget import BaseModelBudget
from fastapi import HTTPException, status
from app.schema.output.month import BaseModelMonth
from sqlalchemy.orm.session import Session
from app.model.tables import Budget, Month
from app.schema.input.month import BaseMonth, BaseMonthUpdate
from app.controller.budget import select_budget_by_budget_id
from app.controller.bu import select_bu


def exists_month(mon: BaseMonth, db: Session):
    ...


def validation(mon: BaseMonth, db: Session) -> None:
    if not select_budget_by_budget_id(budget_id=mon.fk_id_budget, db=db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Budget does not exists."
        )
    if not select_bu(id=mon.fk_id_business_unit, db=db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="BU does not exists."
        )


def insert_month(mon: BaseMonth, db: Session) -> BaseModelMonth:
    validation(mon=mon, db=db)
    month = Month(**mon.dict(by_alias=False))
    db.add(month)
    db.commit()
    db.refresh(month)
    return month


def select_month(id: int, db: Session) -> BaseModelMonth:
    data = db.query(Month).filter(Month.id == id).first()
    return data


def select_month_by_budget_id(budget_id: int, db: Session) -> BaseModelBudget:
    data = db.query(Budget).filter(Budget.id == budget_id).first()
    return data


def update_month(id: int, mon: BaseMonthUpdate, db: Session) -> BaseModelMonth:
    if not select_month(id=id, db=db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Month does not exists."
        )

    validation(mon=mon, db=db)
    month = mon.dict(exclude_none=True, by_alias=False)
    if not month:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No data to change.."
        )

    db.query(Month).filter(Month.id == id).update(month)
    db.commit()
    return db.query(Month).filter(Month.id == id).first()


def delete_month(id: int, db: Session) -> BaseModelMonth:
    month = select_month(id=id, db=db)
    if not month:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Month does not exists."
        )

    data = BaseModelMonth.from_orm(month)
    db.delete(month)
    db.commit()
    return data
