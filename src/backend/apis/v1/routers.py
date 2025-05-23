from fastapi import APIRouter

from src.backend.apis.v1.endpoints import dashboard, data, inference, internal

PREFIX='/api/v1'
TAGS=[PREFIX]


router = APIRouter()

router.include_router(data.router)
router.include_router(internal.router)    
router.include_router(dashboard.router)
router.include_router(inference.router)