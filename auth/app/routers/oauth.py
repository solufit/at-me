from fastapi import APIRouter, Request, Depends, HTTPException, status, Query
from fastapi.security import OAuth2AuthorizationCodeBearer
from fastapi.responses import RedirectResponse
import httpx
import os
import time
import redis
import uuid
import json
import requests

router = APIRouter()

# 環境変数の読み込み
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
FRONTEND_URL = os.getenv("FRONTEND_URL")
AUTHORIZATION_URL = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_URL = "https://oauth2.googleapis.com/token"

connection_pool = redis.ConnectionPool(
    host="atme_auth_redis",
    port=6379,
    db="atme_auth",
)
rc = redis.StrictRedis(connection_pool=connection_pool)

@router.get("/oauth2/login")
async def login_form(redirect: str):
    return f"{AUTHORIZATION_URL}?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}/oauth2/login/callback&scope=openid%20email%20profile%20https://www.googleapis.com/auth/calendar&access_type=offline&prompt=consent"

@router.get("/oauth2/login/callback/")
async def login_callback(code: str = Query(...)):
    async with httpx.AsyncClient() as client:
        token_response = await client.post(
            TOKEN_URL,
            data={
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": f"{REDIRECT_URI}/oauth2/login/callback",
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
            },
        )
    token_response_json = token_response.json()
    if token_response.is_error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=token_response_json,
        )
    
    linkcode=  str(uuid.uuid4())
    rc = redis.Redis(
        host="atme-auth-redis",
        port=6379,
        db=0,
    )
    rc.hmset(
        linkcode,
        {
            "access_token":token_response_json["access_token"],
            "refresh_token":token_response_json["refresh_token"],
            "exp":int(time.time())+3600
        }
    )
    return RedirectResponse(url=f"{FRONTEND_URL}?jwt={token_response_json['id_token']}&linkcode={linkcode}")

@router.get('/oauth2/token')
async def get_token(linkcode: str, secure: str) -> str:
    if secure != os.getenv('SECURE_LOCK'):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN
        )
    rc = redis.Redis(
        host="atme-auth-redis",
        port=6379,
        db=0,
    )
    data = rc.hgetall(linkcode)
    token = json.dumps({key.decode(): value.decode() for key, value in data.items()})
    token = json.loads(token)
    if int(token["exp"]) - int(time.time()) < 300:
        async with httpx.AsyncClient() as client:
            token_response = await client.post(
                TOKEN_URL,
                data={
                    "grant_type": "refresh_token",
                    "refresh_token": token['refresh_token'],
                    "client_id": CLIENT_ID,
                    "client_secret": CLIENT_SECRET,
                },
            )
        token_response_json = token_response.json()
        if token_response.is_error:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=token_response_json,
            )
    
        linkcode=  str(uuid.uuid4())
        rc = redis.Redis(
            host="atme-auth-redis",
            port=6379,
            db=0,
        )
        rc.hmset(
            linkcode,
            {
                "access_token":token_response_json["access_token"],
                "refresh_token":token['refresh_token'],
                "exp":int(time.time()) + 3600
            }
        )
        return token_response_json["access_token"]
    else:
        return token['access_token']