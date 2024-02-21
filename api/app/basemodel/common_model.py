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
    title : str = Field("title", description="titlej")
    etag : str = Field("etag", description="etag")
    note : str = Field("note", description="Note")
    localId : str = Field("localID", description="local user id")
    Taskid : str = Field("task id", description="relational task id")

    class Config:
        orm_mode = True
        
   

    