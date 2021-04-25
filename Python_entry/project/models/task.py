import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
Base = declarative_base()

class Task(Base):
    __tablename__='task'
    taskid = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(length=255))
    category = Column(String(length=255))
    plan = Column(String(length=10))
    etc = Column(String(length=1000))
    finFlag = Column(Integer)
    report = Column(String(length=1000))
