from fastapi import FastAPI
from app.config import cors
from app.resource import bu
from app.resource import auth
from app.resource import employee
from app.resource import budget
from app.resource import approver
from app.model import tables


def create_app():
    app = FastAPI(
        title="backend rwwv",
        version="0.1.0",
        description="Backend para gerenciamento de orçamento.",
    )
    auth.init_app(app=app)
    cors.init_app(app=app)
    tables.init_app(app=app)
    employee.init_app(app=app)
    bu.init_app(app=app)
    budget.init_app(app=app)
    approver.init_app(app=app)
    return app


app = create_app()
