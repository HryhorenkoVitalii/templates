from fastapi import FastAPI

from app.controllers import api_router
from config import ApiConfig as config

api = FastAPI(
    title=config.title,
    docs_url=config.docs_url,
    openapi_url=config.openapi_url,
    redoc_url=config.redoc_url
)

api.include_router(
    router=api_router,
    tags=['v0.1.0'],
)
