from pydantic import BaseModel, Field
import datetime
from typing import Optional, List



class Result(BaseModel):
    success : bool = Field(True, description="Result of tasks")


class atMeBase(BaseModel):
    localId : str = Field("ID", description="User ID")

class Event(atMeBase):
    id : str = Field("ID", description="Event ID")
    calendarID: str = Field("cal id", description="Calendar ID")
    htmlLink : str = Field("HTTP LINK", description="Calendar Web Page")
    starttime : datetime.datetime = Field(datetime.datetime(1910,10,10,10,10,10), description="starttime")
    endtime : datetime.datetime = Field(datetime.datetime(1910,10,10,10,10,10), description="endtime")
    duringtime: int = Field("duringtime")
    title : str = Field("title", description="title")
    etag : str = Field("etag", description="etag")
    note : str = Field("note", description="Note")
    Taskid : str = Field("task id", description="relational task id")
    provider: str = Field(default='atme')

    class Config:
        orm_mode = True

class Task(atMeBase):
    id : str = Field("id", description="Task ID")
    title : str = Field("title", description="task title")
    note : str = Field("note", description="task note")
    updated : datetime.datetime = Field(datetime.datetime(1,1,1,1,1,1), description="updated time and date")
    selfLink : str = Field("URL", description="tasks url")
    parent : str = Field("parent", description="parent")
    position : str = Field("position", description="position")
    status : str = Field("status", description="task status")
    due : datetime.date = Field(datetime.date(1,1,1), description="due date")
    completed : bool = Field(False, description="task completed(y or n)")
    deleted : bool = Field(False, description="if task deleted, it is true")
    hidden : bool = Field(False, description="if the flag is true, the task is hidden")
    duringtime: int = Field(30)
    provider: str = Field(default='atme')

    class Config:
        orm_mode = True

class User(atMeBase):
    email: str
    displayName: str
    photoURL: str
     
   

    