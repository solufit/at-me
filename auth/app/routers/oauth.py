from fastapi import APIRouter, Request, Depends, HTTPException, status, Query
from fastapi.security import OAuth2AuthorizationCodeBearer
from fastapi.responses import RedirectResponse
import httpx
import os

router = APIRouter()

# 環境変数の読み込み
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
FRONTEND_URL = os.getenv("FRONTEND_URL")
AUTHORIZATION_URL = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_URL = "https://oauth2.googleapis.com/token"

oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=AUTHORIZATION_URL,
    tokenUrl=TOKEN_URL
)

@router.get("/oauth2/login")
async def login_form(redirect: str):
    return f"{AUTHORIZATION_URL}?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope=openid%20email%20profile%20https://www.googleapis.com/auth/calendar&access_type=offline&prompt=consent"

@router.get("/oauth2/login/callback/")
async def login_callback(code: str = Query(...)):
    async with httpx.AsyncClient() as client:
        token_response = await client.post(
            TOKEN_URL,
            data={
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": REDIRECT_URI,
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
    return RedirectResponse(url=f"{FRONTEND_URL}?jwt={token_response_json['id_token']}")