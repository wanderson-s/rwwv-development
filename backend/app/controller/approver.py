from fastapi import HTTPException, status
from app.model.tables import Approver, Employee
from app.schema.output.approver import BaseModelApprover
from app.schema.input.approver import BaseApprover
from app.controller.employee import select_employee_by_id
from app.controller.budget import select_budget_by_budget_id
from sqlalchemy.orm.session import Session


def select_check_exists(approver_id: int, budget_id: int, db: Session):
    return (
        db.query(Approver)
        .filter(
            Approver.fk_id_approver == approver_id, Approver.fk_id_budget == budget_id
        )
        .first()
    )


def validade_approver(appro: BaseApprover, db: Session) -> None:
    employee = select_employee_by_id(id=appro.fk_id_approver, db=db)
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            # detail="Employee id does not exists.",
            detail="O funcionário informado não existe.",
        )
    if not select_budget_by_budget_id(budget_id=appro.fk_id_budget, db=db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="O orçamento informado não existe.",  # detail="Budget id does not exists."
        )
    if not employee.can_approve_budget:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Somente uma pessoa com permissões de approve ser selecionada.",
        )


def insert_approver(appro: BaseApprover, db: Session) -> BaseModelApprover:
    validade_approver(appro=appro, db=db)
    if select_check_exists(
        approver_id=appro.fk_id_approver, budget_id=appro.fk_id_budget, db=db
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="O aprovador já existe"
        )
    approver = Approver(**appro.dict(by_alias=False))
    db.add(approver)
    db.commit()
    db.refresh(approver)
    return approver


def select_approver(id: int, db: Session):
    return db.query(Approver).filter(Approver.id == id).first()


def select_approver_by_budget_id(budget_id: int, db: Session):
    return db.query(Approver).filter(Approver.fk_id_budget == budget_id).first()


def select_approver_by_employee_id(employee_id: int, db: Session):
    return db.query(Approver).filter(Approver.fk_id_approver == employee_id).first()


def update_approver(id: int, appro: BaseApprover, db: Session) -> BaseModelApprover:
    validade_approver(appro=appro, db=db)
    approver = db.query(Approver).filter(Approver.id == id).first()
    if not approver:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="O aprovador não existe.",
        )

    db.query(Approver).filter(Approver.id == id).update(
        appro.dict(by_alias=False), synchronize_session=False
    )
    db.commit()
    db.refresh(approver)
    return approver


def delete_approver(id: int, db: Session) -> BaseModelApprover:
    approver = db.query(Approver).filter(Approver.id == id).first()
    if not approver:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="O aprovador não existe.",
        )
    data = BaseModelApprover.from_orm(approver)
    db.delete(approver)
    db.commit()
    return data
