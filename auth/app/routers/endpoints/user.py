from fastapi import APIRouter
from app.basemodel.db_models import user_collection
router = APIRouter()

@router.get('/link')
async def get_link(userId: str,linkcode: str, provider: str):
    # ユーザーIDから該当ユーザーが引っ張ってこれなければ404エラー
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