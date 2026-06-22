from fastapi import APIRouter

router = APIRouter(tags=["Base Router"])
@router.get('/')
async def baserouter():
    return "Welcome to our doctor agent project"

