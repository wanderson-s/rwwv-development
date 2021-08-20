
from app.model.tables import position
from app.model.database import engine
from app.schema.input.position import BaseModelPosition

def select_position():
    query = position.select()
    rows = engine.execute(query).all()
    print(rows)

def insert_position(data: BaseModelPosition):
    insert = position.insert().values(**data.dict())
    rows = engine.execute(insert)
    print(rows)