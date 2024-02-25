from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.core.jwt import get_current_user
router = APIRouter()

@router.post('/check')
async def post_users_check(cred = Depends(get_current_user)):
    return