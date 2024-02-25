from fastapi import APIRouter, Body, Depends, HTTPException
import datetime
from typing import List
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, Field


from app.core.jwt import get_current_user
from app.basemodel.common_model import Task

class Tasks(BaseModel):
    tasks : list[Task] = Field([Task()], description="Task List")


router = APIRouter()

@router.get(
    "",
    description= "get tasks on specific day (deadline)"
)
async def get_task(date: datetime.date = datetime.date(1,1,1) ,cred = Depends(get_current_user)) -> List[Task]:
    result = [
        {
            "id":'asdasd',
            "title":'APIと連携する',
            "note":'',
            "updated": datetime.date(2024,2,24),
            "selfLink": '',
            "parent": '',
            "position": '',
            "status": '',
            "due": datetime.date(2024,2,25),
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
            "position": '',
            "status": '',
            "due": datetime.datetime(2024,2,25,15,0),
            "completed": True,
            "deleted": False,
            "hidden":False
        }
    ]
    return result