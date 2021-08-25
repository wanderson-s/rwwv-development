from databases import Database
from fastapi import FastAPI
from app.config.settings import settings
from app.model.tables import create_table

db = Database(settings.database_uri)


def init_app(app: FastAPI):
    @app.on_event("startup")
    async def startup():
        await db.connect()

    @app.on_event("shutdown")
    async def shutdown():
        await db.disconnect()

    # create_table()
