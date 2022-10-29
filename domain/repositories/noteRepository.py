from database import db
from entities.note import Note
from sqlalchemy.orm import Session
from sqlalchemy import select


def add(note: Note):
    with Session(db.get_engine()) as session:
        session.add(note)
        session.commit()


def get_all():
    with Session(db.get_engine()) as session:
        return session.query(Note).all()


def delete(id):
    with Session(db.get_engine()) as session:
        session.query(Note).filter(Note.id == id).delete(
            synchronize_session=False)
        session.commit()
