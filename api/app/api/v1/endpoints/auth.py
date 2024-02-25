from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.core.jwt import get_current_user
from app.basemodel.common_model import User
router = APIRouter()

@router.get("/info")
async def get_info(cred = Depends(get_current_user)) -> User:
    return {"email":cred['email'],"displayName":cred['name'],"photoURL":cred['picture']}