# We use sqlalchemy so that we don't need to write the queries ourselves, and each and everything will then be handled by
# sqlalchemy

# We use Session for dependency injections so that each function has its own session and session only gets created when needed
from fastapi import Depends
from typing import Annotated
# from .models import Teacher
from sqlmodel import SQLModel # Session
# from sqlalchemy import create_engine
# We will use this for async engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from app.config import settings
# Wrap AsyncSession around sessionmaker
from sqlalchemy.orm import sessionmaker

engine = create_async_engine(
    url=settings.POSTGRES_HOST,
    echo=True,
    # connect_args={"check_same_thread": False}
)

# def craete_table():
#     SQLModel.metadata.create_all(bind=engine)

async def create_table():
    async with engine.begin() as connection:
        await connection.run_sync(SQLModel.metadata.create_all)

# As session is supported by context manager, so we can use with statement
# def get_session():
#     with Session(bind = engine) as session:
#         yield session
#         session.commit()

async def get_session():
    async_session_maker = sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    async with async_session_maker() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_session)]
