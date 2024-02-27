from fastapi import APIRouter

from app.routers.endpoints import google, github, user

api_router = APIRouter()
api_router.include_router(user.router, prefix='/user', tags=["user"])
api_router.include_router(github.router, prefix='/github', tags=["github"])
api_router.include_router(google.router, prefix='/google', tags=['goolge'])