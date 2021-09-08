from app.common.response import BAD_REQUEST_400, CKECK_TOKEN
from fastapi import APIRouter
from fastapi import Depends
from fastapi import FastAPI
from fastapi import status
from fastapi.param_functions import Query
from sqlalchemy.orm.session import Session

from app.controller import auth
from app.config.settings import settings
from app.model.database import get_db

# input
from app.schema.input.auth import BaseLogin

# output
from app.schema.output.auth import BaseModelTokens


def init_app(app: FastAPI):
    router = APIRouter(prefix="/auth")

    @router.post(
        path="/login",
        status_code=status.HTTP_201_CREATED,
        response_model=BaseModelTokens,
        responses=BAD_REQUEST_400,
    )
    async def post_login(user: BaseLogin, db: Session = Depends(get_db)):
        return auth.generate_token(user=user, db=db)

    @router.post(
        path="/refresh-token",
        status_code=status.HTTP_201_CREATED,
        response_model=BaseModelTokens,
        responses=BAD_REQUEST_400,
    )
    async def post_refresh_token(
        refresh_token: str = Query(..., min_length=32, max_length=32),
        db: Session = Depends(get_db),
    ):
        return auth.refresh_token(refresh_token=refresh_token, db=db)

    @router.get("/check-token", responses=CKECK_TOKEN)
    async def get_check_token(
        access_token: str = Query(..., regex=settings.jwt_regex),
        db: Session = Depends(get_db),
    ):
        return auth.check_token(access_token=access_token, db=db)

    app.include_router(router=router, prefix=settings.api_v1, tags=["Authorization"])
