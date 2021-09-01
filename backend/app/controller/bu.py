from sqlalchemy.orm.session import Session
from app.model.tables import BusinessUnit


def select_bu(id: int, db: Session):
    return db.query(BusinessUnit).filter(BusinessUnit.id == id).first()
