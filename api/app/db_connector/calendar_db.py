from sqlalchemy.orm import sessionmaker, Session


from app.db_connector.settings import session as session_maker
    
    
    
    


class calendar_db():

    session : Session = None
    
    def __init__(
        self,
        sessionmk : sessionmaker =  session_maker,

        
    ):
        self.session = sessionmk()

        
    def __delattr__(self, __name: str) -> None:
        self.session.close()



