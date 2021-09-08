from fastapi import HTTPException, status
from app.schema.output.month import BaseModelMonth
from sqlalchemy.orm.session import Session
from app.model.tables import Month
from app.model.enum import EnumMonthType, EnumMonths
from app.schema.input.month import BaseMonth
from app.controller.budget import select_budget_by_budget_id
from app.controller.bu import select_bu


def exists_month(mon: BaseMonth, db: Session):
    ...


def validation(mon: BaseMonth, db: Session) -> None:
    if not select_budget_by_budget_id(budget_id=mon.fk_id_budget, db=db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Budget does not exists."
        )
    if not select_bu(id=mon.fk_id_budget, db=db):
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
