from database import db
from entities.note import Note
from sqlalchemy.orm import Session
from sqlalchemy import select


def add(note: Note):
    with Session(db.get_engine()) as session:
        session.add(note)
        session.commit()


def get_by_name(name: str):
    with Session(db.get_engine()) as session:
        stm = select(Note)

        if name:
            stm = stm.where(Note.name.contains(name))

        return session.scalar(stm)
