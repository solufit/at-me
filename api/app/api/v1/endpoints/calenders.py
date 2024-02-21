from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, Field
from typing import List
import datetime

from app.core.jwt import get_current_user
from app.basemodel.common_model import Event

router = APIRouter()



class Events(BaseModel):
    event : List[Event] = Field([Event()], description="List of event")

    


@router.get(
    "",
    description = "get events of the specified date"
)
async def get_calenders(
    date: datetime.date  = datetime.date(1992, 4, 27),
    cred = Depends(get_current_user)
    ) -> Events:
    print(date)
    return date