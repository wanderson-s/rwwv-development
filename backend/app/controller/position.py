from sqlalchemy.sql.expression import null
from app.model.tables import position
from app.model.database import engine

# INPUT
from app.schema.input.position import BaseModelPosition

# OUTPUT
from app.schema.output.position import ModelPosition


def select_position():
    query = position.select()
    rows = engine.execute(query).fetchall()
    if not rows:
        return None
    return [ModelPosition.from_orm(v) for v in rows]


def insert_position(data: BaseModelPosition):
    insert = position.insert().values(**data.dict())
    rows = engine.execute(insert)
    print(rows)
