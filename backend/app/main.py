from fastapi import FastAPI
from app.model import database


def create_app():
    app = FastAPI(
        title="backend rwwv",
        version="0.1.0",
        description="Backend para gerenciamento de orçamento.",
    )
    database.init_app(app=app)
    return app


app = create_app()
