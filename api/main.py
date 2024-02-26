import uvicorn 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.api import api_router
from app.core import config

app = FastAPI(
    title=config.PROJECT_NAME, openapi_url="/api/v1/openapi.json",
    description = config.DESCRIPTION, version = config.VERSION
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://atme.solufit.net","http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
),

app.include_router(api_router, prefix=config.API_V1_STR)



if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, host="0.0.0.0",reload = True)
    