from app.model.database import db
from app.model.tables import Token
from app.model.tables import SystemUser
from app.model.tables import Employee
from app.model.tables import Permission
from sqlalchemy import select


async def insert_user(user):
    ...


async def select_user():
    stmt = select([Employee, Permission]).select_from(
        Employee.join(Permission, Employee.c.fk_id_permission == Permission.c.id)
    )
    row = await db.fetch_one(stmt)

    return row
