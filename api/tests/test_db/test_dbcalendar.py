import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, close_all_sessions
import os
import datetime
import time
import copy

from db import models
from app.db_connector import calendar_db
from app.basemodel.common_model import Event

default_user : models.User = models.User(
    localId  = "localId",
    email = "email@email.com",
    displayname = "displayName",
    photoIcon = "photoIcon",
    refleshToken = "token"

)


default_calendar : models.Event = models.Event(
    id = "1",
    calendarId = "testtest",
    htmlLink = "t",
    starttime = datetime.datetime(1,1,1,1,1,1),
    endtime = datetime.datetime(1,2,1,1,1,1),
    title = "title",
    etag = "etag",
    note = "note",
    localId = "localid",
    Taskid = "taskid"
    
)


default_calendar_updated : models.Event = models.Event(
    id = "1",
    calendarId = "testtest",
    htmlLink = "t",
    starttime = datetime.datetime(1,1,1,1,1,1),
    endtime = datetime.datetime(1,2,1,1,1,1),
    title = "title-updated",
    etag = "etag",
    note = "note",
    localId = "localid",
    Taskid = "taskid"
    
)


target_calendar : models.Event = models.Event(
    id = "2",
    calendarId = "testtest",
    htmlLink = "t",
    starttime = datetime.datetime(4,1,1,1,1,1),
    endtime = datetime.datetime(6,2,1,1,1,1),
    title = "title-2",
    etag = "etag",
    note = "note",
    localId = "localID",
    Taskid = "taskid"
    
)


class db_calendar_Tests():
    @pytest.fixture(scope="function")
    def db(self):

        if os.path.exists("./test.db"):
            os.remove("./test.db")

        self.session = None
        db_engine = None


        db_engine = create_engine("sqlite:///./test.db")
        db_engine.clear_compiled_cache()


        session : sessionmaker = sessionmaker(db_engine, expire_on_commit=False, autoflush=True)



        #add table to db
        models.Base.metadata.create_all(bind=db_engine)

        with session() as s:

            s.add(copy.deepcopy(default_user))
            s.add(copy.deepcopy(default_calendar))
            s.commit()
            s.flush()
            s.close()



        yield session

 
        close_all_sessions()
        
        db_engine.clear_compiled_cache()
        db_engine.dispose()
        os.remove("./test.db")

        return
    
    def test_cal_load(self, db):


        calendar = calendar_db(
            sessionmk = db,

        )
        result = calendar.load(
            localId = default_calendar.localId
        )

        assert result["1"] == Event.from_orm(default_calendar)

    def test_cal_create_delete(self, db):

        

        calendar = calendar_db(
            sessionmk = db
            
        )
        calendar.create(
            id = target_calendar.id,
            calendarID = target_calendar.calendarId,
            htmlLink = target_calendar.htmlLink,
            starttime = target_calendar.starttime,
            endtime = target_calendar.endtime,
            title = target_calendar.title,
            etag = target_calendar.etag,
            note = target_calendar.note,
            localId = target_calendar.localId,
            Taskid = target_calendar.Taskid
            
        )

        result = calendar.load(
            localId = target_calendar.localId
        )

        assert result["1"] == Event.from_orm(default_calendar)
        assert result["2"] == Event.from_orm(target_calendar)

        calendar.delete(
            id = "1",
            localId = default_calendar.localId
        )

        result = calendar.load(
            localId = target_calendar.localId
        )

        with pytest.raises(KeyError):
            result["1"] == Event.from_orm(default_calendar)

        assert result["2"] == Event.from_orm(target_calendar)

        calendar.delete(
            id = "2",
            localId = target_calendar.localId
        )

        result = calendar.load(
            localId = target_calendar.localId
        )
        with pytest.raises(KeyError):
            result["2"] == Event.from_orm(target_calendar)

                
    def test_cal_update(self, db):
        
     
        calendar = calendar_db(
            sessionmk = db

        )
        calendar.update(
            id = default_calendar.id,
            calendarID = default_calendar.calendarId,
            htmlLink = default_calendar.htmlLink,
            starttime = default_calendar.starttime,
            endtime = default_calendar.endtime,
            title = default_calendar_updated.title,
            etag = default_calendar.etag,
            note = default_calendar.note,
            localId = default_calendar.localId,
            Taskid = default_calendar.Taskid

        )

        result = calendar.load(
            localId = default_calendar.localId
        )

        assert result["1"] == Event.from_orm(default_calendar_updated)
            

            

            

            


            




        
        
    



