from app.schema.input.budget import BaseBudget
from sqlalchemy.orm.session import Session
from app.model.tables import Employee, Budget


def insert_budget(id: int, bud: BaseBudget, db: Session):
    budget = Budget(**bud.dict(), fk_id_employees=id)
    db.add(budget)
    db.commit()
    db.refresh(budget)
    return budget
