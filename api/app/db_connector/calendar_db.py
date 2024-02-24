from sqlalchemy.orm import sessionmaker, Session
import datetime


from app.db_connector.settings import session as session_maker
from db.models import Event
from app.basemodel.common_model import Event as BaseEvent
    
    
    
    


class calendar_db():

    session : Session = None
    
    def __init__(
        self,
        sessionmk : sessionmaker =  session_maker,

        
    ):
        self.session = sessionmk()

        
    def __delattr__(self, __name: str) -> None:
        self.session.close()

        
    def create(
        self,
        localId : str,
        id : str,
        calendarID : str,
        htmlLink : str,
        starttime : datetime.datetime,
        endtime : datetime.datetime,
        etag : str,
        note : str,
        Taskid : str,
        
    ):

        model = Event(
            localId = localId,
            id = id,
            calendarID = calendarID,
            htmlLink = htmlLink,
            starttime = starttime,
            endtime = endtime,
            etag = etag,
            note = note,
            Taskid = Taskid
        )
        
        
        self.session.add(model)        

        self.session.commit()

        
    def load(self, localId: str):

        #result = self.session.query(Event).filter(Event.localId == localId).all()
        result = self.session.query(Event).all()

        return result

        
    def update(
        self,
        localId : str,
        id : str,
        calendarID : str,
        htmlLink : str,
        starttime : datetime.datetime,
        endtime : datetime.datetime,
        etag : str,
        note : str,
        Taskid : str,
    ):
        event : Event = self.session.query(Event).filter(Event.localId == localId).first()

        event.localId = localId
        event.id = id
        event.calendarId = calendarID
        event.htmlLink = htmlLink
        event.starttime = starttime
        event.endtime = endtime
        event.etag = etag
        event.note = note
        event.Taskid = Taskid
        
        self.session.commit()

        
    def delete(self, localId: str, id: str):

        event : Event = self.session.query(Event).filter(Event.localId == localId).filter(Event.id == id).delete()

        self.session.commit()
        
        


        

    

        
        



