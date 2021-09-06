from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from app.model.tables import StatusBudget
from app.controller.budget import select_budget_by_budget_id

# input
from app.schema.input.status_budget import BaseStatusBudget

# output
from app.schema.output.status_budget import BaseModelStatusBudget


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
