from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

from felement.app import app


def remove_session(*args):
    session.rollback()
    session.remove()


def create_session(engine):
    Session = sessionmaker(bind=engine)
    return scoped_session(lambda: Session(autoflush=False, expire_on_commit=False))


Base = declarative_base()

engine = create_engine(app.config['DATABASE_URI'], pool_recycle=600)
session = create_session(engine=engine)
