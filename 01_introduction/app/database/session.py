# We use sqlalchemy so that we don't need to write the queries ourselves, and each and everything will then be handled by
# sqlalchemy

# We use Session for dependency injections so that each function has its own session and session only gets created when needed
from fastapi import Depends
from typing import Annotated
from .models import Teacher
from sqlmodel import SQLModel, Session
from sqlalchemy import create_engine

engine = create_engine(
    url='sqlite:///database.db',
    echo=True,
    connect_args={"check_same_thread": False}
)

def craete_table():
    SQLModel.metadata.create_all(bind=engine)


# As session is supported by context manager, so we can use with statement
def get_session():
    with Session(bind = engine) as session:
        yield session
        session.commit()


SessionDep = Annotated[Session, Depends(get_session)]