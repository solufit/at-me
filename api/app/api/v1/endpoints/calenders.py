from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.core.jwt import get_current_user
router = APIRouter()

@router.get('?date={date}')
async def get_calenders(date: str,cred = Depends(get_current_user)):
    return 