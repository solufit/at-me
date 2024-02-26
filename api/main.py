import uvicorn 
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.v1.api import api_router
from app.core import config

app = FastAPI(
    title=config.PROJECT_NAME, openapi_url="/api/v1/openapi.json",
    description = config.DESCRIPTION, version = config.VERSION
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
),

app.include_router(api_router, prefix=config.API_V1_STR)