# We use sqlalchemy so that we don't need to write the queries ourselves, and each and everything will then be handled by
# sqlalchemy

from sqlmodel import SQLModel
from sqlalchemy import create_engine

engine = create_engine(
    url='sqlite:///database.db',
    echo=True,
    connect_args={"check_same_thread": False}
)

def craete_table():
    from .models import Teacher
    SQLModel.metadata.create_all(bind=engine)