from sqlalchemy import Column, Integer, String, Time, Date, Text, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import CHAR, TEXT
from sqlalchemy.dialects.mysql import BOOLEAN
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.dialects.mysql import TEXT
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASE = "mysql+pymysql"
USER = os.getenv('MYSQL_USER')
PASSWORD = os.getenv('MYSQL_PASSWORD')
HOST = os.getenv('MYSQL_HOST')
PORT = "3306"
DB_NAME = os.getenv('MYSQL_DATABASE')

DATABASE_URL = "{}://{}:{}@{}:{}/{}".format(
    DATABASE, USER, PASSWORD, HOST, PORT, DB_NAME
)

Engine = create_engine(DATABASE_URL,pool_size=100,max_overflow=0)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    localId = Column(String(25), primary_key=True, unique=True)
    email = Column(String(30), unique=True)
    displayname = Column(String(30))
    photoIcon = Column(String(500))
    refleshToken = Column(String(500))

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(String(25), primary_key=True, unique=True)
    kind = Column(String(25))
    localId = Column(String(25))
    title = Column(TEXT)
    duetime = Column(TIMESTAMP)
    description = Column(TEXT)

class WorktimeWeek(Base):
    __tablename__ = 'worktimeWeek'
    id = Column(Integer, primary_key=True)
    worktimeStart = Column(Time, nullable=False)
    worktimeEnd = Column(Time, nullable=False)
    localID = Column(Text)

class WorktimeDate(Base):
    __tablename__ = 'worktimeDate'
    id = Column(Integer, primary_key=True)
    targetDate = Column(Date, nullable=False)
    worktimeStart = Column(Time, nullable=False)
    worktimeEnd = Column(Time, nullable=False)
    localID = Column(Text)

class Calendar(Base):
    __tablename__ = 'calendar'
    id = Column(Integer, primary_key=True)
    starttime = Column(TIMESTAMP, nullable=False)
    endtime = Column(TIMESTAMP, nullable=False)
    title = Column(Text)
    note = Column(Text)
    localID = Column(Text)
    calID = Column(Text)