from typing import List
from fastapi import APIRouter
from fastapi import FastAPI

# CONTROLLER
from app.controller import position as controller

# SCHEMA
from app.schema.input.position import BaseModelPosition
from app.schema.output.position import ModelPosition


def init_app(app: FastAPI) -> None:
    router = APIRouter(prefix="/v1", tags=["Position"])

    @router.get("/position", response_model=List[ModelPosition])
    def get_position():
        return controller.select_position()

    @router.post("/position")
    def post_position(position: BaseModelPosition):
        return controller.insert_position(data=position)

    app.include_router(router=router)
