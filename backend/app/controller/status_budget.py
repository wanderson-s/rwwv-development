from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from app.model.tables import Budget, StatusBudget
from app.controller.budget import select_budget_by_budget_id

# input
from app.schema.input.status_budget import BaseStatusBudget, BasestatusBudgetToUpdate

# output
from app.schema.output.status_budget import BaseModelStatusBudget
from app.schema.output.budget import BaseModelBudget


def change_status_to_disable(budget_id: int, db: Session) -> None:
    db.query(StatusBudget).filter(StatusBudget.fk_id_budget == budget_id).update(
        {"current": False}, synchronize_session=False
    )
    db.commit()


def insert_status_budget(
    status_bud: BaseStatusBudget, db: Session
) -> BaseModelStatusBudget:
    if not select_budget_by_budget_id(budget_id=status_bud.fk_id_budget, db=db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Budget id does not exists."
        )
    if status_bud.current:
        change_status_to_disable(budget_id=status_bud.fk_id_budget, db=db)
    status_budget = StatusBudget(**status_bud.dict(by_alias=False))
    db.add(status_budget)
    db.commit()
    db.refresh(status_budget)
    return status_budget


def select_status_budget_by_id(id: int, db: Session) -> BaseModelStatusBudget:
    return db.query(StatusBudget).filter(StatusBudget.id == id).first()


def select_status_budget_by_budget_id(budget_id: id, db: Session) -> BaseModelBudget:
    return db.query(Budget).filter(Budget.id == budget_id).scalar()


def update_status_budget(
    id: int, status_bud: BasestatusBudgetToUpdate, db: Session
) -> BaseModelStatusBudget:
    status = select_status_budget_by_id(id=id, db=db)
    if not status:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Status Budget id does not exists.",
        )
    row = status_bud.dict(exclude_none=True)
    if not row:
        raise HTTPException(
            status_code=status.HTTP_206_PARTIAL_CONTENT, detail="No data to change."
        )
    db.query(StatusBudget).filter(StatusBudget.id == id).update(
        row, synchronize_session=False
    )
    db.commit()
    db.refresh(status)
    return status


def delete_status_budget(id: int, db: Session) -> BaseModelStatusBudget:
    if not select_status_budget_by_id(id=id, db=db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Id does not exists."
        )
    status = db.query(StatusBudget).filter(StatusBudget.id == id).first()
    data = BaseModelStatusBudget.from_orm(status)
    db.delete(status)
    db.commit()
    return data
