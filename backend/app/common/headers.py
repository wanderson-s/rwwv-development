from jwt import decode
from fastapi import status
from fastapi import Header
from fastapi import HTTPException
from app.config.settings import settings
from app.schema.input.common.headers import BaseAuthorization


def get_claims(token: str) -> BaseAuthorization:
    token_pure = token.split()[1] if "bearer" in token.lower() else token
    try:
        claims = decode(token_pure, key=settings.jwt_secret, algorithms="RS256")
        return BaseAuthorization(**claims)
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(error),
        )


def decode_token(
    token: str = Header(
        ...,
        alias="Authorization",
        regex=settings.jwt_regex,
        description=("The authorization token is used to validate your identity."),
    )
) -> BaseAuthorization:
    return get_claims(token=token)


def decode_token_is_admin(
    token: str = Header(
        ...,
        alias="Authorization",
        regex=settings.jwt_regex,
        description=("The authorization token is used to validate your identity."),
    )
) -> BaseAuthorization:
    user = get_claims(token=token)
    if not user.role.is_admin:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized, you must be an admin.",
        )
    return user
