from typing import Union

from fastapi import FastAPI

from src.config import *

from src.health.router import router as health_router

app = FastAPI(
    title=app_name,
    version=app_version,
)

app.include_router(health_router)
