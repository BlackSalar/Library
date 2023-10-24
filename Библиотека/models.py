from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, mapped_column, column_property
from sqlalchemy import  Column, Integer, String,ForeignKey, DateTime, Table
from sqlalchemy import create_engine

import tkinter.messagebox as mb


class Enginer():
    database=""
    engine=create_engine("sqlite:///")   
 
# создаем модель, объекты которой будут храниться в бд
class Base(DeclarativeBase):pass

    
class Books_table(Base):
    __tablename__ = "Books" 
    Book_id = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    Author = Column(String)
    State=Column(String)    
    Reader_id=Column(Integer,ForeignKey("Readers.Reader_id"))
    Reader=relationship("Readers_table")
    Logbooks=relationship("Logbook_table") 
         
class Readers_table(Base):
    __tablename__="Readers"
    Reader_id=Column(Integer, primary_key=True, index=True)
    Surname=Column(String)
    Name=Column(String)
    Patronymic=Column(String) 
    Books=relationship("Books_table",back_populates="Reader")
    Logbooks=relationship("Logbook_table")
class Logbook_table(Base):
    __tablename__="Logbook"
    Logbook_id=Column(Integer,primary_key=True,index=True)
    Date=Column(DateTime)
    Condition=Column(String)    
    Reader_id=Column(Integer,ForeignKey("Readers.Reader_id"))
    Reader=relationship("Readers_table")
    Book_id=Column(Integer,ForeignKey("Books.Book_id"))
    Book=relationship("Books_table")
    
          

      
    