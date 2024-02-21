from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
import json

from app.basemodel.common_model import Result


from app.core.jwt import get_current_user
router = APIRouter()


@router.post(
    "/",
    description="Sync with google apis",
    response_model = Result,
    responses = {
        500: {
            "model": Result
        }
    }
)
async def post_sync(cred = Depends(get_current_user)):
    sync_status : bool = True

    if sync_status != True:
        return JSONResponse(
            status_code=500,
            content = json.dumps(Result(success = False).dict())
            
        )

    return Result(success = True)