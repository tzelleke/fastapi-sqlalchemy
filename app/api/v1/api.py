from fastapi import APIRouter

from .address import router as address_router

router = APIRouter()
router.include_router(address_router, prefix="/addresses")
