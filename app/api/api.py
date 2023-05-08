from importlib import import_module

from fastapi import (
    APIRouter,
    Depends,
)
from sqlalchemy.sql import text
from sqlmodel import Session

from app.core.config import API_VERSION
from app.db import get_session

api = import_module(f".{API_VERSION}", package="app.api")
router = APIRouter()


@router.get(
    "/db-version",
    response_model=dict,
    tags=["Healthcheck"],
)
async def db_version(session: Session = Depends(get_session)):
    version = session.execute(text("select sqlite_version()")).one()

    return {"version": version}


router.include_router(api.router, prefix=f"/{API_VERSION}")
