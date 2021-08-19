from fastapi import FastAPI
from app.resource import position


def create_app():
    app = FastAPI(
        title="backend rwwv",
        version="0.1.0",
        description="Backend para gerenciamento de orçamento.",
    )
    position.init_app(app=app)
    return app


if __name__ == "app.main":
    app = create_app()

