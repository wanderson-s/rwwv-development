from fastapi import FastAPI
from app.config import cors
from app.model import database
from app.resource import auth


def create_app():
    app = FastAPI(
        title="backend rwwv",
        version="0.1.0",
        description="Backend para gerenciamento de orçamento.",
    )
    cors.init_app(app=app)
    database.init_app(app=app)
    auth.init_app(app=app)
    return app


app = create_app()
