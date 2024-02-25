""" google.py  """
import datetime
import os
import requests
from fastapi import APIRouter, Depends, HTTPException
from typing import List

from app.core.jwt import get_current_user
from app.basemodel.common_model import Event

router = APIRouter()

AUTH_API = os.getenv("AUTH_API")
SECURE_LOCK = os.getenv("SECURE_LOCK")


@router.get("/calender", description="get events of the specified date")
async def get_calender(
    userlink: str, date: datetime.date = datetime.date(1992, 4, 27), cred=Depends(get_current_user)
) -> List[Event]:
    """

    Args:
        userlink (str): _description_
        date (datetime.date, optional): _description_. Defaults to datetime.date(1992, 4, 27).
        cred (_type_, optional): _description_. Defaults to Depends(get_current_user).

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    print(cred['email'])
    access_token = requests.get(f"{AUTH_API}/oauth2/token?linkcode={userlink}&secure={SECURE_LOCK}", timeout=(3.0, 7.5))
    if access_token.status_code == 403:
        raise HTTPException(status_code=403)
    access_token = access_token.text
    res = requests.get(
        f"https://content.googleapis.com/calendar/v3/calendars/primary/events?timeMin={datetime.datetime(date.year, date.month, date.day,0,0,0).isoformat()}Z&timeMax={datetime.datetime(date.year, date.month, date.day,23,59,59).isoformat()}Z",
        timeout=(3.0, 7.5),
        headers={'Authorization': f"Bearer {access_token}"}
    )
    contens = [ Event(localId=item['id'],id=item['id'],calendarID=item['iCalUID'],htmlLink=item['htmlLink'],starttime=item['start']['dateTime'],endtime=item['end']['dateTime'],duringtime=((datetime.datetime.fromisoformat(item['end']['dateTime']) - datetime.datetime.fromisoformat(item['start']['dateTime'])).seconds // 60),title=item['summary'],etag=item['etag'],note=(item['description'] if 'description' in item else ''),Taskid='')  for item in res.json()["items"] if 'dateTime' in item['start']]
    return contens
