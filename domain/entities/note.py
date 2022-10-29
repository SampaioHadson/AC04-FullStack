from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from database import db  

Base = db.get_base()

class Note(Base):
    __tablename__ = "Note"

    id = Column(Integer, primary_key = True)
    name = Column(String(120))
    description = Column(String)