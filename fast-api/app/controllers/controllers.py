from typing import Any

from fastapi import APIRouter

from app.controllers.responses import DefaultResponse
from app.model import ExampleRepository

router = APIRouter()


@router.get("/", name='hello_world', response_model=DefaultResponse)
def hello_world():
    payload: list[Any] = [{"msg": "Hello world!"}]
    return DefaultResponse(success=True, payload=payload)
