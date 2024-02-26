from fastapi import FastAPI
from auth.app.routers.api import api_router
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    ),
app.include_router(api_router)