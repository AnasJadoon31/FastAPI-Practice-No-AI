from sqlalchemy import desc
from sqlalchemy import asc
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.models import ModelTeacherUpdate
from app.database.models import Teacher


class TeacherService:
    def __init__(self, session: AsyncSession):
        self.session = session
        pass

    async def get_all(self, sort: str | None) -> list[Teacher]:
        teachers = select(Teacher)

        if sort == "asc":
            teachers = teachers.order_by(asc(Teacher.name))

        if sort == "desc":
            teachers = teachers.order_by(desc(Teacher.name))

        result = await self.session.scalars(teachers)

        return result.all()

    async def get(self, id: int) -> Teacher | None:
        return await self.session.get(Teacher, id)

    async def add(self, data: ModelTeacherUpdate) -> Teacher:
     
        self.session.add(data)
        await self.session.commit()
        await self.session.refresh(data)

        return data

    async def update(self, id: int, data: ModelTeacherUpdate) -> Teacher:
        db_teacher = await self.session.get(Teacher, id)

        if db_teacher is None:
            return None

        db_teacher.sqlmodel_update(data.model_dump(exclude_unset=True))

        self.session.add(db_teacher)
        await self.session.commit()
        await self.session.refresh(db_teacher)

        return db_teacher

    async def patch(self, id: int, data: ModelTeacherUpdate) -> Teacher:
        db_teacher = await self.session.get(Teacher, id)

        if db_teacher is None:
            return None

        db_teacher.sqlmodel_update(data.model_dump(exclude_unset=True))

        self.session.add(db_teacher)
        await self.session.commit()
        await self.session.refresh(db_teacher)

        return db_teacher

    async def delete(self, id: int) -> dict:
        db_teacher = await self.session.get(Teacher, id)

        if db_teacher is None:
            return {"success": "False"}

        await self.session.delete(db_teacher)
        await self.session.commit()

        return {"success": "True"}
