from fastapi import APIRouter
from app.basemodel.db_models import user_collection
router = APIRouter()

@router.get('/link')
async def get_link(userId: str,linkcode: str, provider: str):
    return

@router.get('/profile')
async def get_profile(userId: str, linkcode: str, provider: str):
    return