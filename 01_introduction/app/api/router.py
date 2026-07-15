from app.database.models import Teacher
from sqlalchemy import select
from schemas import TeacherGet
from schemas import TeacherUpdate
from fastapi import HTTPException
from app.database.models import ModelTeacherUpdate
from schemas import TeacherDelete
from app.database.session import SessionDep
from sqlalchemy import asc, desc
from fastapi import APIRouter

router = APIRouter()

@router.get("/teachers")
async def get_teachers(session: SessionDep, sort: str | None = None):
    teacher_names = []
    teacher_names = await session.scalars(select(Teacher)).all()
    print("teacher names", teacher_names)
    if sort == "asc":
        sorted_teacher_names = await session.scalars(
            select(Teacher.name).order_by(asc(Teacher.name))
        ).all()
        return sorted_teacher_names
    elif sort == "desc":
        sorted_teacher_names = await session.scalars(
            select(Teacher.name).order_by(desc(Teacher.name))
        ).all()
        return sorted_teacher_names
    else:
        return teacher_names

@router.get("/teachers/{teacher_id}", response_model=TeacherGet)
async def get_teacher(teacher_id: int, session: SessionDep):
    teacher = await session.get(Teacher, teacher_id)
    if teacher is None:
        raise HTTPException(
            status_code=404, detail=f"Teacher with id {teacher_id} not found"
        )
    return teacher

@router.post("/teachers")
async def add_teacher(teacher: Teacher, session: SessionDep):
    session.add(teacher)
    await session.commit()
    await session.refresh(teacher)
    return teacher

@router.put("/teachers/{teacher_id}", response_model=Teacher)
async def update_teacher(teacher_id: int, data: TeacherUpdate, session: SessionDep):
    db_teacher= await session.get(Teacher, teacher_id)
    db_teacher.sqlmodel_update(data.model_dump()) # It will take data without ** because it can process pydantic models directly
    session.add(db_teacher)
    await session.commit()
    await session.refresh(db_teacher)
    return db_teacher

@router.patch("/teachers/{teacher_id}", response_model=Teacher)
async def patch_teacher(teacher_id: int, data: ModelTeacherUpdate, session: SessionDep):
    db_teacher = await session.get(Teacher, teacher_id)
    db_teacher.sqlmodel_update(data.model_dump(exclude_unset=True))
    session.add(db_teacher)
    await session.commit()
    await session.refresh(db_teacher)
    return db_teacher

@router.delete("/teachers/{teacher_id}", response_model=TeacherDelete)
async def delete_teacher(teacher_id: int, session: SessionDep):
    db_teacher = session.get(Teacher, teacher_id)
    if db_teacher is None:
        raise HTTPException(
            status_code=404, detail=f"Teacher with id {teacher_id} not found"
        )
    await session.delete(db_teacher)
    await session.commit()
    return {"success": "True"}