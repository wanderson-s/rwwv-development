from fastapi import APIRouter
from fastapi import FastAPI


def init_app(app: FastAPI) -> None:
    router = APIRouter(prefix="/v1", tags=["Position"])

    @router.get("/position")
    def get_position():
        return {"message": "ok"}

    app.include_router(router=router)
