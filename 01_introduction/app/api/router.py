from dependencies import ServiceDep
from app.database.models import Teacher
from schemas import TeacherGet
from schemas import TeacherUpdate
from fastapi import HTTPException
from app.database.models import ModelTeacherUpdate
from schemas import TeacherDelete
from fastapi import APIRouter

router = APIRouter()


@router.get("/teachers")
async def get_teachers(service:ServiceDep, sort: str | None = None):
    teachers = await service.get_all(sort)

    return teachers


@router.get("/teachers/{teacher_id}", response_model=TeacherGet)
async def get_teacher(teacher_id: int, service: ServiceDep):
    teacher = await service.get(teacher_id)

    if teacher is None:
        raise HTTPException(status_code=404, detail=f"Teacher with id {teacher_id} not found")

    return teacher


@router.post("/teachers")
async def add_teacher(teacher: Teacher, service: ServiceDep):
    teacher = await service.add(teacher)

    return teacher


@router.put("/teachers/{teacher_id}", response_model=Teacher)
async def update_teacher(teacher_id: int, data: TeacherUpdate, service: ServiceDep):
    teacher = await service.update(teacher_id, data)

    if teacher is None:
        raise HTTPException(status_code=404, detail=f"Teacher with id {teacher_id} not found")

    return teacher


@router.patch("/teachers/{teacher_id}", response_model=Teacher)
async def patch_teacher(teacher_id: int, data: ModelTeacherUpdate, service: ServiceDep):
    teacher = await service.patch(teacher_id, data)

    if teacher is None:
        raise HTTPException(status_code=404, detail=f"Teacher with id {teacher_id} not found")

    return teacher


@router.delete("/teachers/{teacher_id}", response_model=TeacherDelete)
async def delete_teacher(teacher_id: int, service: ServiceDep):
    result = await service.delete(teacher_id)

    if result == {"success": "False"}:
        raise HTTPException(status_code=404, detail=f"Teacher with id {teacher_id} not found")

    return result
