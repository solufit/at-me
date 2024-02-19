from sqlalchemy import Column, Integer, String, Time, Date, Text, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import CHAR, TEXT
from sqlalchemy.dialects.mysql import BOOLEAN
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
import os

DATABASE = "postgresql+psycopg2"
USER = "postgres"
PASSWORD = "postgres"
HOST = "db"
PORT = "5432"
DB_NAME = "atme"

DATABASE_URL = "{}://{}:{}@{}:{}/{}".format(
    DATABASE, USER, PASSWORD, HOST, PORT, DB_NAME
)

Engine = create_engine(DATABASE_URL,pool_size=100,max_overflow=0)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    localId = Column(TEXT, primary_key=True, unique=True)
    email = Column(TEXT, unique=True)
    displayname = Column(TEXT)
    photoIcon = Column(TEXT)
    refleshToken = Column(TEXT)

class TaskList(Base):
    __tablename__ = "taskList"
    id = Column(TEXT, primary_key=True, unique=True)
    kind = Column(TEXT)
    title = Column(TEXT)
    updated = Column(TIMESTAMP)
    selfLink = Column(TEXT)
    etag = Column(TEXT)
    localId = Column(TEXT, ForeignKey("users.localId"))
    

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(TEXT, primary_key=True, unique=True)
    localId = Column(TEXT), ForeignKey("users.localId")
    kind = Column(TEXT)
    title = Column(TEXT)
    note = Column(TEXT)
    etag = Column(TEXT)
    updated = Column(TIMESTAMP)
    selfLink = Column(TEXT)
    parent = Column(TEXT)
    position = Column(TEXT)
    status = Column(TEXT)
    due = Column(Date)
    completed = Column(TIMESTAMP)
    deleted = Column(BOOLEAN)
    hidden = Column(BOOLEAN)
    

class WorktimeWeek(Base):
    __tablename__ = 'worktimeWeek'
    id = Column(Integer, primary_key=True, autoincrement=True)
    worktimeStart = Column(Time, nullable=False)
    worktimeEnd = Column(Time, nullable=False)
    localId = Column(TEXT), ForeignKey("users.localId")

class WorktimeDate(Base):
    __tablename__ = 'worktimeDate'
    id = Column(Integer, primary_key=True, autoincrement=True)
    targetDate = Column(Date, nullable=False)
    worktimeStart = Column(Time, nullable=False)
    worktimeEnd = Column(Time, nullable=False)
    localId = Column(TEXT), ForeignKey("users.localId")

class Calendar(Base):
    __tablename__ = 'calendar'
    id = Column(Integer, primary_key=True)
    starttime = Column(TIMESTAMP, nullable=False)
    endtime = Column(TIMESTAMP, nullable=False)
    title = Column(Text)
    note = Column(Text)
    calID = Column(Text)
    localId = Column(TEXT), ForeignKey("users.localId")