""" google.py  """
import datetime
import os
import requests
from fastapi import APIRouter, Depends, HTTPException
from typing import List

from app.core.jwt import get_current_user
from app.basemodel.common_model import Task

router = APIRouter()

AUTH_API = os.getenv("AUTH_API")
SECURE_LOCK = os.getenv("SECURE_LOCK")


@router.get("/issues", description="get events of the specified date")
async def get_issues(userlink: str) -> List[Task]:
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
    access_token = requests.get(f"{AUTH_API}/github/token?linkcode={userlink}&secure={SECURE_LOCK}", timeout=(3.0, 7.5))
    print(access_token.text.replace('"',''))
    if access_token.status_code == 403:
        raise HTTPException(status_code=403)
    elif access_token.status_code == 401:
        raise HTTPException(status_code=401)
    access_token = access_token.text.replace('"','')
    res = requests.get(
        f" https://api.github.com/issues",
        timeout=(3.0, 7.5),
        headers={"Accept": "application/vnd.github+json",'Authorization': f"Bearer {access_token}","X-GitHub-Api-Version": "2022-11-28"}
    )
    def convert_datetime_str(utc):
        utc_time = datetime.datetime.strptime(utc,"%Y-%m-%dT%H:%M:%SZ" )
        jst_time = utc_time + datetime.timedelta(hours=9)
        jst_string = jst_time.strftime("%Y-%m-%dT%H:%M:%S")
        return jst_string
    result = [
        Task(
            id= issue['id'],
            provider= 'github',
            title= issue['title'],
            note= issue['body'] if issue['body'] != None else '',
            updated= convert_datetime_str(issue['updated_at']),
            selfLink= issue['html_url'],
            parent= '',
            position= '',
            status= '',
            duringtime= 0,
        )
        for issue in res.json()
    ]
    print(f'Authorization Bearer {access_token}')
    return result

@router.get("/profile", description="get user profile")
async def get_profile(userlink: str):
    return