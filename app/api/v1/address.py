from typing import List

from fastapi import (
    APIRouter,
    Depends,
)
from sqlmodel import (
    Session,
    select,
)
from starlette.status import HTTP_200_OK

from app.db import get_session
from app.models import Address

router = APIRouter()


@router.get(
    "/",
    response_model=List[Address],
    status_code=HTTP_200_OK,
    tags=["Addresses"],
)
async def list_addresses(
    *,
    session: Session = Depends(get_session),
):
    addresses = session.exec(select(Address)).all()

    return addresses
