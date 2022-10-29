from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine("sqlite:///local.db", echo=True, future=True)
Base = declarative_base()


def get_engine():
    return engine


def get_base():
    return Base


def start():
    Base.metadata.create_all(engine)
