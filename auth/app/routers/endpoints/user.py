from fastapi import APIRouter, HTTPException
from app.basemodel.db_models import user_collection
router = APIRouter()
import requests
from app.core import config
import os

@router.get('/link')
async def get_link(userId: str,linkcode: str, provider: str):
    # ユーザーIDから該当ユーザーが引っ張ってこれなければ404エラー
    user = user_collection.find_one({"userId":userId})
    if user is None:
        raise HTTPException(status_code=404,detail="User Data is not defind")
    SECURE_LOCK = os.getenv('SECURE_LOCK')
    match provider:
        case 'google':
            # Google からユーザー情報の取得
            user_collection.update_one({"userId":userId},{"providers.google.linkcode":linkcode})
        case 'github':
            access_token = requests.get(f"{config.AUTH_API}/github/token?linkcode={linkcode}&secure={SECURE_LOCK}", timeout=(3.0, 7.5))
            if access_token.status_code == 403:
                raise HTTPException(status_code=403)
            elif access_token.status_code == 401:
                raise HTTPException(status_code=401)
            access_token = access_token.text.replace('"','')
            res = requests.get(
                f" https://api.github.com/user",
                timeout=(3.0, 7.5),
                headers={"Accept": "application/vnd.github+json",'Authorization': f"Bearer {access_token}","X-GitHub-Api-Version": "2022-11-28"}
            )
            content = res.json()
            providerinfo = {
                "photoURL":content['avatar_url'],
                "displayName":content['name'],
                "email":content['login'],
                "linkcoede": linkcode
            }
            user_collection.update_one({"userId":userId},{"providers.github": providerinfo})
    return

@router.get('/profile')
async def get_profile(userId: str):
    # ユーザーIDをもとにアカウントデータを返却
    # ユーザーIDが存在しない場合は404エラーを返却
    return

@router.get('/account')
async def get_account(linkcode: str, provider: str):
    # 各プロバイダーで認証して認証できたらユーザーIDを返却
    # できなければ新規作成
    return