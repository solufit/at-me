from fastapi import APIRouter, Body, Depends, HTTPException
import datetime
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, Field


from app.core.jwt import get_current_user
from app.basemodel.common_model import Task

class Tasks(BaseModel):
    tasks : list[Task] = Field([Task()], description="Task List")


router = APIRouter()

@router.get(
    "/",
    description= "get tasks on specific day (deadline)"
)
async def get_task(date: datetime.date = datetime.date(1,1,1) ,cred = Depends(get_current_user)) -> Tasks:
    return

@router.get('/deadline', description="Get a list of tasks due within a week")
async def get_tasks_deadline(cred = Depends(get_current_user)) -> Tasks:
    return

@router.get('/near', description="Get a list of tasks with deadlines in the last week")
async def get_tasks_near(cred = Depends(get_current_user)) -> Tasks:
    return
