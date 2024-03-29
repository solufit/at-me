from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, Field
from typing import List
import datetime
import requests
import os

from app.core.jwt import get_current_user
from app.basemodel.common_model import Event

router = APIRouter()
AUTH_API = os.getenv("AUTH_API")
SECURE_LOCK = os.getenv("SECURE_LOCK")

async def get_google_calendar(userlink :str, date: datetime.date) -> List[Event]:
    access_token = requests.get(f"{AUTH_API}/google/token?linkcode={userlink}&secure={SECURE_LOCK}", timeout=(3.0, 7.5))
    if access_token.status_code == 403:
        raise HTTPException(status_code=403)
    elif access_token.status_code == 401:
        raise HTTPException(status_code=401,detail="Authentication to the linked account is required")
    access_token = access_token.text
    res = requests.get(
        f"https://content.googleapis.com/calendar/v3/calendars/primary/events?timeMin={datetime.datetime(date.year, date.month, date.day,0,0,0).isoformat()}Z&timeMax={datetime.datetime(date.year, date.month, date.day,23,59,59).isoformat()}Z",
        timeout=(3.0, 7.5),
        headers={'Authorization': f"Bearer {access_token}"}
    )
    if 'items' in res.json():
        contents = [ Event(localId=item['id'],id=item['id'],calendarID=item['iCalUID'],htmlLink=item['htmlLink'],starttime=item['start']['dateTime'],endtime=item['end']['dateTime'],duringtime=((datetime.datetime.fromisoformat(item['end']['dateTime']) - datetime.datetime.fromisoformat(item['start']['dateTime'])).seconds // 60),title=item['summary'],etag=item['etag'],note=(item['description'] if 'description' in item else ''),Taskid='',provider='GoogleCalender')  for item in res.json()["items"] if 'dateTime' in item['start']]
        return contents
    else:
        return

async def get_atme_calendar(userid :str, date: datetime.date) -> List[Event]:
    testdata = [
        {
            "id": '',
            "calemderID": '',
            "htmlLink": '',
            "starttime": datetime.datetime(date.year, date.month, date.day,10,30,0),
            "endtime": datetime.datetime(date.year, date.month, date.day,13,45,0),
            'duringtime': ((datetime.datetime(date.year, date.month, date.day,10,30,0) - datetime.datetime(date.year, date.month, date.day,13,45,0)).seconds) // 60,
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

@router.get(
    "",
    description = "get events of the specified date"
)
async def get_calendars(
    token: str,
    date: datetime.date  = datetime.date(1992, 4, 27),
    ) -> List[Event]:
    user = requests.get(f"{AUTH_API}/session/verify?token={token}&secure={SECURE_LOCK}", timeout=(3.0, 7.5)).json()
    if user is None:
        raise HTTPException(status_code=401)
    match user["calendarProvider"]:
        case 'atme':
            return await get_atme_calendar(user['userId'],date)
        case 'GoogleCalendar':
            return await get_google_calendar(user["providers"]["google"]["linkcode"],date)

@router.get('/dot')
async def get_dot(cred = Depends(get_current_user)):
    return {
        "schedules" : [
            datetime.date(2024,2,2),
            datetime.date(2024,2,4),
            datetime.date(2024,2,7),
            datetime.date(2024,2,8),
            datetime.date(2024,2,9),
            datetime.date(2024,2,12),
            datetime.date(2024,2,15),
            datetime.date(2024,2,16),
            datetime.date(2024,2,19),
            datetime.date(2024,2,20),
            datetime.date(2024,2,22),
            datetime.date(2024,2,24),
            datetime.date(2024,2,25),
            datetime.date(2024,2,26),
            datetime.date(2024,2,27),
            datetime.date(2024,2,28),
            datetime.date(2024,3,1) 
        ],
        "tasks": [
            datetime.date(2024,2,24),
            datetime.date(2024,2,25),
            datetime.date(2024,2,27),
            datetime.date(2024,2,29),
            datetime.date(2024,3,1),
            datetime.date(2024,3,2) 
        ]
    }