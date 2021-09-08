from hashlib import md5
from fastapi import HTTPException, status
from datetime import datetime, timedelta
from uuid import uuid1
from fastapi.param_functions import Query
from sqlalchemy.orm.session import Session

import jwt

from app.config.settings import settings
from app.model.tables import Employee
from app.model.tables import Token

# input
from app.schema.input.auth import BaseLogin

# output
from app.schema.output.auth import BaseModelTokens


# methods not callable on the resource
def mount_body_token(employee: Employee):
    exp = datetime.utcnow() + timedelta(hours=1)
    body = {
        "user": {
            "id": employee.id,
            "sub": employee.email,
            "first_name": employee.first_name,
            "last_name": employee.last_name,
            "position": employee.position.value,
        },
        "role": {
            "is_admin": employee.is_admin,
            "active": employee.active,
            "can_simulate_budget": employee.can_simulate_budget,
            "can_submit_budget": employee.can_submit_budget,
            "can_approve_budget": employee.can_approve_budget,
            "can_read_budget": employee.can_read_budget,
        },
        "exp": exp,
    }
    return body


def disable_tokens(id: int, db: Session):
    db.query(Token).filter(Token.fk_id_employees == id, Token.enable == True).update(
        {"enable": False}
    )
    db.commit()


def insert_token(values: dict, db: Session):
    token = Token(**values)
    db.add(token)
    db.commit()


def create_token(employee: Employee, db: Session):
    body = mount_body_token(employee=employee)
    access = jwt.encode(body, settings.jwt_secret, algorithm="HS256")
    tokens = {"access_token": access, "refresh_token": str(uuid1()).replace("-", "")}
    data = {**tokens, "exp": body["exp"], "fk_id_employees": employee.id}
    disable_tokens(id=employee.id, db=db)
    insert_token(values=data, db=db)
    return tokens


def get_token_enable(id: int, db: Session):
    data = (
        db.query(Token).filter(Token.fk_id_employees == id, Token.enable == True).first()
    )
    if data and data.exp > datetime.utcnow():
        return data
    return {}


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


def generate_token(user: BaseLogin, db: Session) -> BaseModelTokens:
    user.password = md5(user.password.encode()).hexdigest()
    employee = (
        db.query(Employee)
        .filter(Employee.email == user.email, Employee.password == user.password)
        .first()
    )
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid user or password."
        )
    token = get_token_enable(id=employee.id, db=db)
    return token if token else create_token(employee=employee, db=db)


def refresh_token(
    db: Session, refresh_token: str = Query(..., min_length=32, max_length=32)
) -> BaseModelTokens:
    token = (
        db.query(Token)
        .filter(Token.refresh_token == refresh_token, Token.enable == True)
        .first()
    )
    if not token:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid user or password."
        )
    if token and token.exp > datetime.utcnow():
        return token

    employee = db.query(Employee).filter(Employee.id == token.fk_id_employees).first()
    return create_token(employee=employee, db=db)


def check_token(access_token: str, db: Session) -> dict:
    token = db.query(Token).filter(Token.access_token == access_token).first()
    if not token:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token.")
    try:
        jwt.decode(jwt=access_token, key=settings.jwt_secret, algorithms="HS256")
        return {"detail": "Valid token."}
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_206_PARTIAL_CONTENT,
            detail=str(error) or "Invalid token.",
        )
        raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT, detail=str(error))
