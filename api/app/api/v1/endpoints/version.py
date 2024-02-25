from fastapi import APIRouter
from pydantic import BaseModel
from app.core.config import VERSION, PROJECT_NAME


router = APIRouter()


class Version(BaseModel):
    title : str = PROJECT_NAME
    version : str = VERSION

    
@router.get(
    path = "/",
    description = "Return API Version",
    response_model = Version
)
async def version():
    return Version()