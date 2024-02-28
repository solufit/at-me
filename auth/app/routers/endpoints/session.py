from fastapi import APIRouter, HTTPException
import os
import redis
import time
import uuid
from app.core import config
from app.basemodel.db_models import user_collection, User

router = APIRouter()

async def get_generate_token(userId: str):
    rc = redis.Redis(
        host="atme-auth-redis",
        port=6379,
        db=1,
    )
    token = str(uuid.uuid4())
    rc.set(token,userId,ex=3600)
    return token

@router.get('/verify')
async def get_verify_token(token: str, secure: str) -> User:
    if secure != os.getenv("SECURE_LOCK"):
        raise HTTPException(status_code=401)
    rc = redis.Redis(
        host="atme-auth-redis",
        port=6379,
        db=1,
    )
    userId = rc.get(token)
    if userId is None:
        raise HTTPException(status_code=401)
    else:
        user = await user_collection.find_one({"userId":userId.decode('utf-8')})
        if user is None:
            raise HTTPException(status_code=404,detail="User Data is not defind")
        else:
            rc.expire(token,3600)
            return user

@router.get('/invalid')
async def get_invalid(token: str):
    rc = redis.Redis(
        host="atme-auth-redis",
        port=6379,
        db=1,
    )
    rc.delete(token)
    return