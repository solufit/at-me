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

    def _convert_model(self, result: list[Event]) -> dict[str, BaseEvent]:

        result_dict = {}
        for i in result:
            convert = BaseEvent().from_orm(i)
            result_dict[convert.id] = convert

            
        return result_dict

        
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
        title: str,
        
    ):

        model = Event(
            localId = localId,
            id = id,
            calendarId = calendarID,
            htmlLink = htmlLink,
            starttime = starttime,
            endtime = endtime,
            etag = etag,
            note = note,
            Taskid = Taskid,
            title = title
        )
        
        
        self.session.add(model)        

        self.session.commit()

        
    def load(self, localId: str):

        result = self.session.query(Event).filter(Event.localId == localId).all()
        #result = self.session.query(Event).all()

        #for i in result:
        #    if i.localId != localId:
        #        result.remove(i)
                

        complete = self._convert_model(result)

        return complete

        
    def update(
        self,
        localId : str,
        id : str,
        calendarID : str,
        title : str,
        htmlLink : str,
        starttime : datetime.datetime,
        endtime : datetime.datetime,
        etag : str,
        note : str,
        Taskid : str,
    ):
        event : Event = self.session.query(Event).filter(Event.localId == localId)\
            .filter(Event.id == id).filter(Event.calendarId == calendarID).first()

        event.localId = localId
        event.id = id
        event.calendarId = calendarID
        event.htmlLink = htmlLink
        event.starttime = starttime
        event.endtime = endtime
        event.etag = etag
        event.note = note
        event.Taskid = Taskid
        event.title = title

        
        self.session.commit()


    def delete(self, localId: str, id: str):

        event : Event = self.session.query(Event).filter(Event.localId == localId).filter(Event.id == id).delete()

        self.session.commit()

        


            

            

        
        


        

    

        
        



