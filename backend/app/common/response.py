from pydantic import BaseModel
from fastapi import status


class Base(BaseModel):
    detail: str


OK_200 = {status.HTTP_200_OK: {"model": Base, "description": "Success"}}

PARTIAL_CONTENT_206 = {
    status.HTTP_206_PARTIAL_CONTENT: {"model": Base, "description": "Partial Content."}
}


BAD_REQUEST_400 = {
    status.HTTP_400_BAD_REQUEST: {"model": Base, "description": "Invalid data."}
}

UNAUTHORIZED_401 = {
    status.HTTP_401_UNAUTHORIZED: {"model": Base, "description": "Invalid data."}
}

CKECK_TOKEN = {**OK_200, **PARTIAL_CONTENT_206, **BAD_REQUEST_400}
