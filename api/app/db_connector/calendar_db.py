from sqlalchemy.orm import sessionmaker, Session


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
        localId = BaseEvent.localId,
        id = BaseEvent.id,
        calendarID = BaseEvent.calendarID,
        htmlLink = BaseEvent.htmlLink,
        starttime = BaseEvent.starttime,
        endtime = BaseEvent.endtime,
        etag = BaseEvent.etag,
        note = BaseEvent.note,
        Taskid = BaseEvent.Taskid,
        
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

        
    def load(self, localId: BaseEvent.localId):

        result = self.session.query(Event).filter(Event.localId == localId).all()

        return result

        
    def update(
        self,
        localId = BaseEvent.localId,
        id = BaseEvent.id,
        calendarID = BaseEvent.calendarID,
        htmlLink = BaseEvent.htmlLink,
        starttime = BaseEvent.starttime,
        endtime = BaseEvent.endtime,
        etag = BaseEvent.etag,
        note = BaseEvent.note,
        Taskid = BaseEvent.Taskid,
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

        

    

        
        



