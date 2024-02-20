from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.core.jwt import get_current_user
router = APIRouter()

@router.get('?date={date}')
async def get_task(date: str,cred = Depends(get_current_user)):
    return

@router.get('/deadline')
async def get_tasks_deadline(cred = Depends(get_current_user)):
    return

@router.get('/near')
async def get_tasks_near(cred = Depends(get_current_user)):
    return
