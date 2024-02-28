from fastapi import APIRouter
from app.api.v1.endpoints import auth, sync, tasks, users, version, google, github,calendars

api_router = APIRouter()
api_router.include_router(auth.router, prefix='/auth', tags=["auth"])
api_router.include_router(google.router, prefix='/google', tags=['goolge'])
api_router.include_router(github.router, prefix='/github', tags=['github'])
api_router.include_router(calendars.router, prefix="/calendars", tags=["calendars"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(sync.router, prefix="/sync", tags=["sync"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
api_router.include_router(version.router, tags=["version"])