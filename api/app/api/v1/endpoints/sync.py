from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.core.jwt import get_current_user
router = APIRouter()

@router.post('/sync')
async def post_sync(cred = Depends(get_current_user)):
    return