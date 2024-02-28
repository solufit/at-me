from fastapi import APIRouter, Body, Depends, HTTPException
import datetime
from typing import List
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, Field
import requests
import os

from app.core.jwt import get_current_user
from app.basemodel.common_model import Task

class Tasks(BaseModel):
    tasks : list[Task] = Field([Task()], description="Task List")


router = APIRouter()
AUTH_API = os.getenv("AUTH_API")
SECURE_LOCK = os.getenv("SECURE_LOCK")

async def get_atme_tasks(userId: str,date: datetime.date) -> List[Task]:
    result = [
        {
            "id":'asdasd',
            "title":'APIと連携する',
            "note":'',
            "updated": datetime.datetime(2024,2,24),
            "selfLink": '',
            "parent": '',
            "position": '',
            "status": '',
            "due": datetime.datetime(2024,2,25),
            "completed": False,
            "deleted": False,
            "hidden":False,
            "duringtime": 30
        },
        {
            "id":'asdasdasd',
            "title":'UIを頑張って作る',
            "note":'',
            "updated": datetime.datetime(2024,2,24),
            "selfLink": '',
            "parent": '',
            "position": '',
            "status": '',
            "due": datetime.datetime(2024,2,25),
            "completed": True,
            "deleted": False,
            "hidden":False
        }
    ]
    return result

async def get_github_issues(userlink :str) -> List[Task]:
    access_token = requests.get(f"{AUTH_API}/github/token?linkcode={userlink}&secure={SECURE_LOCK}", timeout=(3.0, 7.5))
    if access_token.status_code == 403:
        raise HTTPException(status_code=403)
    elif access_token.status_code == 401:
        raise HTTPException(status_code=401)
    access_token = access_token.text.replace('"','')
    res = requests.get(
        f" https://api.github.com/issues",
        timeout=(3.0, 7.5),
        headers={"Accept": "application/vnd.github.html+json",'Authorization': f"Bearer {access_token}","X-GitHub-Api-Version": "2022-11-28"}
    )
    def convert_datetime_str(utc):
        utc_time = datetime.datetime.strptime(utc,"%Y-%m-%dT%H:%M:%SZ" )
        jst_time = utc_time + datetime.timedelta(hours=9)
        jst_string = jst_time.strftime("%Y-%m-%dT%H:%M:%S")
        return jst_string
    result = [
        Task(
            id= issue['id'],
            provider= 'GithubIssues',
            title= issue['title'],
            note= issue['body_html'] if issue['body_html'] != None else '',
            updated= convert_datetime_str(issue['updated_at']),
            selfLink= issue['html_url'],
            parent= f"{issue['url'].split('/')[4]}/{issue['url'].split('/')[5]}" ,
            position= '',
            status= '',
            duringtime= 0,
        )
        for issue in res.json()
    ]
    return result

@router.get(
    "",
    description= "get tasks on specific day (deadline)"
)
async def get_tasks(token: str, date: datetime.date = datetime.date(1,1,1)) -> List[Task]:
    user = requests.get(f"{AUTH_API}/session/verify?token={token}&secure={SECURE_LOCK}", timeout=(3.0, 7.5)).json()
    match user["taskProvider"]:
        case 'atme':
            result = await get_atme_tasks(user['userId'],date)
        case 'GithubIssues':
            result = await get_github_issues(user["providers"]["github"]["linkcode"])
    return result


@router.get('/deadline', description="Get a list of tasks due within a week")
async def get_tasks_deadline(cred = Depends(get_current_user)) -> List[Task]:
    return

@router.get('/near', description="Get a list of tasks with deadlines in the last week")
async def get_tasks_near(cred = Depends(get_current_user)) -> List[Task]:
    return

@router.get('/complite', description="Task update as complited")
async def get_tasks_complite(taskid: str,cred = Depends(get_current_user)) -> List[Task]:
    result = [
        {
            "id":'asdasd',
            "title":'APIと連携する',
            "note":'',
            "updated": datetime.datetime(2024,2,24,14,0),
            "selfLink": '',
            "parent": '',
            "provider": 'atme',
            "position": '',
            "status": '',
            "due": datetime.datetime(2024,2,25,15,0),
            "completed": False,
            "deleted": False,
            "hidden":False,
            "duringtime": 30
        },
        {
            "id":'asdasdasd',
            "title":'UIを頑張って作る',
            "note":'',
            "updated": datetime.datetime(2024,2,24,14,0),
            "selfLink": '',
            "parent": '',
            "provider": 'atme',
            "position": '',
            "status": '',
            "due": datetime.datetime(2024,2,25,15,0),
            "completed": True,
            "deleted": False,
            "hidden":False
        }
    ]
    return result