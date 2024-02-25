from sqlalchemy.orm import sessionmaker, Session
import datetime


from app.db_connector.settings import session as session_maker
from db.models import Task
from app.basemodel.common_model import Task as BaseTask
    
    
    
    


class task_db():

    session : Session = None
    
    def __init__(
        self,
        sessionmk : sessionmaker =  session_maker,

        
    ):
        self.session = sessionmk()

        
    def __delattr__(self, __name: str) -> None:
        self.session.close()

    def _convert_model(self, result: list[Task]) -> dict[str, BaseTask]:

        result_dict = {}
        for i in result:
            convert = BaseTask().from_orm(i)
            result_dict[convert.id] = convert

            
        return result_dict

        
    def create(
        self,
        localId : str,
        id : str,
        kind : str,
        title : str,
        note : str,
        etag : str,
        updated : datetime.datetime,
        selfLink : str,
        parent : str,
        position : str,
        status : str,
        due : datetime.date,
        completed : datetime.datetime,
        deleted : bool,
        hidden: bool
        
    ):

        model = Task(
            localId = localId,
            id = id,
            kind = kind,
            title = title,
            note = note,
            etag = etag,
            updated = updated,
            selfLink = selfLink,
            parent = parent,
            position = position,
            status = status,
            due = due,
            completed = completed,
            deleted = deleted,
            hidden = hidden
        )
        
        
        self.session.add(model)        

        self.session.commit()

        
    def load(self, localId: str):

        result = self.session.query(Task).filter(Task.localId == localId).all()
        complete = self._convert_model(result)

        return complete

        
    def update(
        self,
        localId : str,
        id : str,
        kind : str,
        title : str,
        note : str,
        etag : str,
        updated : datetime.datetime,
        selfLink : str,
        parent : str,
        position : str,
        status : str,
        due : datetime.date,
        completed : datetime.datetime,
        deleted : bool,
        hidden: bool
    ):
        task: Task = self.session.query(Task).filter(Task.localId == localId)\
            .filter(Task.id == id).first()

        task.id = id,
        task.localId = localId,
        task.kind = kind,
        task.title = title,
        task.note = note,
        task.etag = etag,
        task.updated = updated,
        task.selfLink = selfLink,
        task.parent = parent,
        task.position = position,
        task.status = status,
        task.due = due,
        task.completed = completed,
        task.deleted = deleted,
        task.hidden = hidden
        




        
        self.session.commit()


    def delete(self, localId: str, id: str):

        task : Task = self.session.query(Task).filter(Task.localId == localId).filter(Task.id == id).delete()

        self.session.commit()
