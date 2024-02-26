from fastapi import APIRouter, HTTPException, status, Query
from fastapi.responses import RedirectResponse
import httpx
import os
import time
import redis
import uuid
import json
import requests
from app.core import config
router = APIRouter()

# 環境変数の読み込み
CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
AUTHORIZATION_URL = "https://github.com/login/oauth/authorize"
TOKEN_URL = "https://github.com/login/oauth/access_token"

connection_pool = redis.ConnectionPool(
    host="atme_auth_redis",
    port=6379,
    db="atme_auth",
)
rc = redis.StrictRedis(connection_pool=connection_pool)

@router.get("/login")
async def login_form():
    return f"{AUTHORIZATION_URL}?client_id={CLIENT_ID}&scopes=user:email repo issues:read&redirect_uri={config.AUTH_HOST}/github/callback"

@router.get("/install")
async def install_form():
    return "https://github.com/apps/at-me-app/installations/new"

def callback(token_response):
    token_response_json = token_response.json()
    if token_response.status_code != 200:
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
            "exp":int(time.time()) + int(token_response_json["expires_in"]),
            "exp_refresh": int(time.time()) + int(token_response_json["refresh_token_expires_in"])
        }
    )
    return token_response_json, linkcode

@router.get("/callback")
async def login_callback(code: str = Query(...)):
    token_response = requests.post(
        TOKEN_URL,
        headers={"Accept":"application/json"},
        data={
            "code": code,
            "redirect_uri": f"{config.AUTH_HOST}/github/callback",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        },
    )
    token_response_json, linkcode = callable(token_response)
    return RedirectResponse(url=f"{config.FRONTEND_URL}?jwt={token_response_json["access_token"]}&linkcode={linkcode}&provider=github&type=login")

@router.get('/callback_install')
async def get_callback_install(code: str = Query(...)):
    token_response = requests.post(
        TOKEN_URL,
        headers={"Accept":"application/json"},
        data={
            "code": code,
            "redirect_uri": f"{config.AUTH_HOST}/github/callback",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        },
    )
    token_response_json, linkcode = callable(token_response)
    return RedirectResponse(url=f"{config.FRONTEND_URL}?jwt={token_response_json["access_token"]}&linkcode={linkcode}&provider=github&type=auth")


@router.get('/token')
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
    if not "access_token" in token:
        raise HTTPException(status_code=401, detail="LinkCode is invalid")
    if int(token["exp"]) - int(time.time()) < 300:
        raise HTTPException(status_code=401,detail="Refresh Token is expired")
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
                "refresh_token":token_response_json['refresh_token'],
                "exp":int(time.time()) + int(token_response_json["expires_in"]), # アクセストークンの有効期限が切れるまでの時間
                "exp_refresh": int(time.time()) + int(token_response_json["refresh_token_expires_in"])
            }
        )
        return token_response_json["access_token"]
    else:
        return token['access_token']