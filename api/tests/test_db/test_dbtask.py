import pytest
import copy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import os
import datetime

from db import models
from app.db_connector import task_db
from app.basemodel.common_model import Task

default_user : models.User = models.User(
    localId  = "localId",
    email = "email@email.com",
    displayname = "displayName",
    photoIcon = "photoIcon",
    refleshToken = "token"

)

default_task : models.Task = models.Task(    
    localId = "localId",
    id = "id",
    title = "title",
    note = "notes",
    updated = datetime.datetime(2023, 12, 20, 20, 59),
    selfLink = "selflink",
    parent = "parent",
    position = "position",
    status = "status",
    due = datetime.date(2023, 12, 24),
    completed = False,
    completedTime = datetime.datetime(1, 1, 1, 1, 1, 1),
    deleted = False,
    hidden = False 
)

default_task_updated : models.Task = models.Task(    
    localId = "localId",
    id = "id",
    title = "title-updated",
    note = "notes-updated",
    updated = datetime.datetime(2, 1, 1, 1, 1, 1),
    selfLink = "selflink-update",
    parent = "parent-update",
    position = "position-update",
    status = "status-update",
    due = datetime.datetime(1,1,1),
    completedTime = datetime.datetime(1, 1, 1, 1, 1, 1),
    completed = True,
    deleted = False,
    hidden = False 
)


default_task_nearline : models.Task = models.Task(    
    localId = "localId",
    id = "id",
    title = "title-updated",
    note = "notes-updated",
    updated = datetime.datetime(2, 1, 1, 1, 1, 1),
    selfLink = "selflink-update",
    parent = "parent-update",
    position = "position-update",
    status = "status-update",
    due = datetime.date.today() - datetime.timedelta(days = 3),
    completed = True,
    completedTime = datetime.datetime(1, 1, 1, 1, 1, 1),
    deleted = False,
    hidden = False 
)

target_task : models.Task = models.Task(
    localId = "localId",
    id = "targetid" ,

    title = "title",
    note = "notes",
    updated = datetime.datetime(1, 2, 1, 1, 1, 1),
    selfLink = "selflink",
    parent = "parent",
    position = "position",
    status = "status",
    due = datetime.date(2, 1, 1),
    completed = False,
    completedTime = datetime.datetime(1, 1, 1, 1, 1, 1),
    deleted = False,
    hidden = False
)


class db_task_Tests():
    @pytest.fixture(scope="function")
    def db(self):
        if os.path.exists("./test.db"):
            os.remove("./test.db")

        db_engine = create_engine("sqlite:///./test.db")
        session : sessionmaker = sessionmaker(db_engine)

        #add table to db
        models.Base.metadata.create_all(bind=db_engine)

        with session() as s:
            s: Session = s

            s.add(copy.deepcopy(default_user))
            s.add(copy.deepcopy(default_task))
            s.commit()

        yield session
        
        db_engine.dispose()
        os.remove("./test.db")

        return
    
    def test_tasks_load(self, db):


        task = task_db(
            sessionmk = db

        )
        result = task.load(
            localId = default_task.localId
        )

        assert result["id"] == Task.from_orm(default_task)

    def test_task_create_delete(self, db):
 

        task = task_db(
            sessionmk= db
            
        )
        task.create(
            localId = target_task.localId, 
            id = target_task.id,
            title = target_task.title,
            note = target_task.note,
            updated = target_task.updated,
            selfLink = target_task.selfLink,
            parent = target_task.parent,
            position = target_task.position,
            status = target_task.status,
            due = target_task.due,
            completed = target_task.completed,
            deleted = target_task.deleted,
            hidden = target_task.hidden,
            kind=target_task.kind,
            etag = target_task.etag           
                
        )

        result = task.load(
            localId = target_task.localId
        )

        assert result["id"] == Task.from_orm(default_task)
        assert result["targetid"] == Task.from_orm(target_task)

        task.delete(
            id = default_task.id,
            localId = default_task.localId
        )

        result = task.load(
            localId = target_task.localId
        )
        with pytest.raises(KeyError):
            result["id"] == Task.from_orm(default_task)

        assert result["targetid"] == Task.from_orm(target_task)

        task.delete(
            id = target_task.id,
            localId = target_task.localId
        )

        result = task.load(
            localId = target_task.localId
        )
        with pytest.raises(KeyError):
            result["targetid"] == Task.from_orm(target_task)

    
    def test_task_update(self, db):

            task = task_db(
                sessionmk = db

            )
            task.update(
                localId = default_task.localId,
                id = default_task.id,
                title = default_task_updated.title,
                note = default_task_updated.note,
                updated = default_task_updated.updated,
                selfLink = default_task_updated.selfLink,
                parent = default_task_updated.parent,
                position = default_task_updated.position,
                status = default_task_updated.status,
                due = default_task_updated.due,
                completed = default_task_updated.completed,
                deleted = default_task_updated.deleted,
                hidden = default_task_updated.hidden,
                etag = default_task_updated.etag,
                kind = default_task_updated.kind

            )

            result = task.load(
                localId = default_task.localId
            )

            assert result[default_task.id] == Task.from_orm(default_task_updated)

    def test_get_deadline_tasks(self, db):
        with db() as session:
            session : Session = session # for completion

            task = task_db(
                session = session,

            )
            result = task.get_deadline_tasks(
                localId = default_task.localId
            )

            assert result[1] == Task.from_orm(default_task)

            
    def test_get_nearline_tasks(self, db):
        with db() as session:
            session : Session = session # for completion


            task = task_db(
                session = session,

            )

            task.create(
                localid = default_task_nearline.localId,
                id = default_task_nearline.id,  
                title = default_task_nearline.title,
                note = default_task_nearline.note,
                updated = default_task_nearline.updated,
                selfLink = default_task_nearline.selfLink,
                parent = default_task_nearline.parent,
                position = default_task_nearline.position,
                status = default_task_nearline.status,
                due = default_task_nearline.due,
                completed = default_task_nearline.completed,
                deleted = default_task_nearline.deleted,
                hidden = default_task_nearline.hidden
                
            )            
            

            result = task.get_nearline_tasks(
                localId = default_task.localId
            )

            assert result[1] == Task.from_orm(default_task_nearline)
        

        

                
            

            

            

            


            




        
        
    

