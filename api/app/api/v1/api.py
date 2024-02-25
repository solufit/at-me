from fastapi import APIRouter

from app.api.v1.endpoints import auth, calenders, sync, tasks, users, version, google

api_router = APIRouter()
api_router.include_router(auth.router, prefix='/auth', tags=["auth"])
api_router.include_router(google.router, prefix='/google', tags=['goolge'])
api_router.include_router(calenders.router, prefix="/calenders", tags=["calenders"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(sync.router, prefix="/sync", tags=["sync"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
api_router.include_router(version.router, tags=["version"])