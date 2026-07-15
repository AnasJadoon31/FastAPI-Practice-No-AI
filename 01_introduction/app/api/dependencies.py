from app.database.session import get_session
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from app.services.TeacherService import TeacherService


SessionDep = Annotated[AsyncSession, Depends(get_session)]

def get_teacher_service(session: SessionDep):
    return TeacherService(session)

ServiceDep = Annotated[TeacherService, Depends(get_teacher_service)]