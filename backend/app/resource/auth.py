from fastapi import APIRouter
from fastapi import FastAPI

from app.config.settings import settings
from app.controller import auth


def init_app(app: FastAPI):
    router = APIRouter(prefix="/auth")

    @router.post(path="/login")
    async def post_login():
        ...

    @router.post(path="/refresh-token")
    async def post_refresh_token():
        ...

    @router.get(path="/checks-token")
    async def get_check_token():
        return await auth.select_user()

    app.include_router(router=router, prefix=settings.api_v1, tags=["Authorization"])
