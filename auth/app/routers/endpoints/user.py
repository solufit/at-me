from fastapi import APIRouter, HTTPException
from app.basemodel.db_models import user_collection, User
router = APIRouter()
import requests
from app.core import config
import os
import uuid
from app.routers.endpoints import google, github
import datetime

@router.get('/link')
async def get_link(userId: str,linkcode: str, provider: str) -> User:
    # ユーザーIDから該当ユーザーが引っ張ってこれなければ404エラー
    user = await user_collection.find_one({"userId":userId})
    if user is None:
        raise HTTPException(status_code=404,detail="User Data is not defind")
    SECURE_LOCK = os.getenv('SECURE_LOCK')
    access_token = await github.get_token(linkcode=linkcode,secure=SECURE_LOCK)
    if type(access_token) is not str:
        raise HTTPException(status_code=403)
    access_token = access_token.replace('"','')
    match provider:
        case 'google':
            res = requests.get(
                "https://www.googleapis.com/oauth2/v1/userinfo",
                headers={'Authorization': f"Bearer {access_token}"}
            )
            content = res.json()
            providerinfo = {
                "id": content['email'], # Githubの返り値を確認（重複のない一意のIDが欲しい）
                "photoURL":content['picture'],
                "displayName":content['name'],
                "email":content['email'],
                "linkcoede": linkcode
            }
            await user_collection.update_one({"userId":userId},{"$set":{"providers.google":providerinfo}})
        case 'github':
            res = requests.get(
                f" https://api.github.com/user",
                timeout=(3.0, 7.5),
                headers={"Accept": "application/vnd.github+json",'Authorization': f"Bearer {access_token}","X-GitHub-Api-Version": "2022-11-28"}
            )
            content = res.json()
            providerinfo = {
                "id": content['id'], # Githubの返り値を確認（重複のない一意のIDが欲しい）
                "photoURL":content['avatar_url'],
                "displayName":content['name'],
                "email":content['login'],
                "linkcoede": linkcode
            }
            await user_collection.update_one({"userId":userId},{"$set":{"providers.github": providerinfo}})
    return await user_collection.find_one({"userId":userId})

@router.get('/profile')
async def get_profile(userId: str) -> User:
    user = await user_collection.find_one({"userId":userId})
    if user is None:
        raise HTTPException(status_code=404,detail="User Data is not defind")
    return user

async def create_user(provider,providerinfo):
    providers = {
        "atme": {
            "id":"",
            "photoURL":"",
            "displayName":"",
            "email":"",
            "linkcode":""
        },
        "google": {
            "id":"",
            "photoURL":"",
            "displayName":"",
            "email":"",
            "linkcode":""
        },
        "github": {
            "id":"",
            "photoURL":"",
            "displayName":"",
            "email":"",
            "linkcode":""
        }
    }
    providers[provider] = providerinfo
    user = {
        "userId":str(uuid.uuid4()),
        "displayName":providerinfo["displayName"],
        "email":providerinfo["email"],
        "photoURL":providerinfo['photoURL'],
        "calenderProvider":'atme',
        "taskProvider":'atme',
        "lastlogin": provider,
        "providers":providers,
        "created_at":datetime.datetime.now()
    }
    await user_collection.insert_one(user)
    return user

@router.get('/account')
async def get_account(linkcode: str, provider: str) -> User:
    # 各プロバイダーで認証して認証できたらユーザーIDを返却
    # できなければ新規作成
    SECURE_LOCK = os.getenv('SECURE_LOCK')
    access_token = await github.get_token(linkcode=linkcode,secure=SECURE_LOCK)
    if type(access_token) is not str:
        raise HTTPException(status_code=403)
    access_token = access_token.replace('"','')
    match provider:
        case 'google':
            res = requests.get(
                "https://www.googleapis.com/oauth2/v1/userinfo",
                headers={'Authorization': f"Bearer {access_token}"}
            )
            content = res.json()
            user = await user_collection.find_one({"providers.google.id":content['email']})
            if not user:
                user = await create_user(provider=provider,providerinfo={"id":content["email"],"displayName":content["name"],"photoURL":content['picture'],"email":content['email'],"linkcode":linkcode})
        case 'github':
            res = requests.get(
                f" https://api.github.com/user",
                timeout=(3.0, 7.5),
                headers={"Accept": "application/vnd.github+json",'Authorization': f"Bearer {access_token}","X-GitHub-Api-Version": "2022-11-28"}
            )
            content = res.json()
            user = await user_collection.find_one({"providers.github.id":content['id']}) # 要確認
            if not user:
                # 新規ユーザー作成
                user = await create_user(provider=provider,providerinfo={"id":content["id"],"displayName":content["name"],"photoURL":content['avatar_url'],"email":content['login'],"linkcode":linkcode})
    return user

@router.post('/set_provider')
async def post_set_provider(userId: str, calenderProvider: str, taskProvider: str) -> User:
    user = await user_collection.find_one_and_update({"userId":userId},{"$set":{"calenderProvider":calenderProvider,"taskProvider":taskProvider}})
    return user