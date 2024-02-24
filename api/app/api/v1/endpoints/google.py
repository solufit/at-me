from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, Field
from typing import List
import datetime
import os
import requests

from app.core.jwt import get_current_user
from app.basemodel.common_model import Event

router = APIRouter()

AUTH_API = os.getenv('AUTH_API')
SECURE_LOCK = os.getenv('SECURE_LOCK')

@router.get(
    "/calender",
    description = "get events of the specified date"
)
async def get_calender(
    userlink: str,
    date: datetime.date  = datetime.date(1992, 4, 27),
    cred = Depends(get_current_user)
    ) -> List[Event]:
    access_token = requests.get(f'{AUTH_API}/oauth2/token?linkcode={userlink}&secure={SECURE_LOCK}')
    if access_token.status_code == 403:
        raise HTTPException(status_code=403)
    access_token = access_token.text

    ## 
    ## 現時刻以降の予定を「早い順」に並び替えて返却
    testdata = [
        {
            "id": '',
            "calemderID": '',
            "htmlLink": '',
            "starttime": datetime.datetime(2024,2,24,11,0),
            "endtime": datetime.datetime(2024,2,24,23,0),
            'duringtime': ((datetime.datetime(2024,2,24,23,0) - datetime.datetime(2024,2,24,11,0)).seconds) // 60,
            "title": '@me フロントエンド開発',
            "etag": '',
            "note": 'ハッカソン開発',
            "Taskid": ''
        },
        {
            "id": '',
            "calemderID": '',
            "htmlLink": '',
            "starttime": datetime.datetime(2024,2,24,19,0),
            "endtime": datetime.datetime(2024,2,24,19,15),
            'duringtime': ((datetime.datetime(2024,2,24,19,15) - datetime.datetime(2024,2,24,19,0)).seconds) // 60,
            "title": 'MTG',
            "etag": '',
            "note": '全体ミーティング',
            "Taskid": ''
        }
    ]
    return testdata