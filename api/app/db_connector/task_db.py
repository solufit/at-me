from sqlalchemy.orm import sessionmaker, Session, Query
import datetime
import copy


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

    def _load(self, localId: str): 
        result = self.session.query(Task).filter(Task.localId == localId).all()

        return result

        
    def load(self, localId: str):

        result = self._load(localId)
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

        task.id = copy.deepcopy(id)
        task.localId = copy.deepcopy(localId)
        task.kind = copy.deepcopy(kind)
        task.title = copy.deepcopy(title)
        task.note = copy.deepcopy(note)
        task.etag = copy.deepcopy(etag)
        task.updated = copy.deepcopy(updated)
        task.selfLink = copy.deepcopy(selfLink)
        task.parent = copy.deepcopy(parent)
        task.position = copy.deepcopy(position)
        task.status = copy.deepcopy(status)
        task.due = copy.deepcopy(due)
        task.completed = copy.deepcopy(completed)
        task.deleted = copy.deepcopy(deleted)
        task.hidden = copy.deepcopy(hidden)
        




        
        self.session.commit()


    def delete(self, localId: str, id: str):

        task : Task = self.session.query(Task).filter(Task.localId == localId).filter(Task.id == id).delete()

        self.session.commit()

    def get_deadline_tasks(self, localId: str):
        today = datetime.date.today()
        seven_days_later = today + datetime.timedelta(days=7)

        query = self.session.query(Task).filter(Task.localId == localId)

        result = query.filter(Task.due >= today).filter(Task.due <= seven_days_later)\
            .filter(Task.completed == False).all()

        result = self._convert_model(result)

        return result

        
    def get_nearline_tasks(self, localId: str):
        today = datetime.date.today()
        seven_days_before = today - datetime.timedelta(days=7)

        query: Query  = self.session.query(Task).filter(Task.localId == localId)

        result = query.filter(Task.due >= seven_days_before).filter(Task.due < today)\
            .all()

        result = self._convert_model(result)

        return result


        
        
