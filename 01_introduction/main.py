# from rich.progress import TimeElapsedColumn
# from app.database.models import ModelTeacherUpdate
# from sqlalchemy import asc
# from sqlalchemy import desc
# from app.database.session import SessionDep
# from typing import Annotated
# from sqlalchemy import select
# from app.database.models import Teacher
# from app.database.session import get_session
# from fastapi import Depends
# from sqlmodel import Session
from app.api.router import router
from app.database.session import create_table
from contextlib import asynccontextmanager
from fastapi import FastAPI #, HTTPException
from scalar_fastapi import get_scalar_api_reference
import uvicorn
from app.db import Database
from rich import print, panel

# from typing import Any
# from app.schemas import (
#     # TeacherAdd,
#     TeacherDelete,
#     TeacherGet,
#     # TeacherPatch,
#     TeacherUpdate,
# )
# from app.db import save, teachers


# We use lifespan to use context manager within fastapi app, and it works with async (independently)
@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    print(panel.Panel("Server is starting", border_style="green"))
    # We will use the table generator function from the session.py
    await create_table()
    yield
    print(panel.Panel("Server is stopping", border_style="red"))


app = FastAPI(lifespan=lifespan_handler)

db = Database()


app.include_router(router)

@app.get("/scalar")
def get_scalar():
    return get_scalar_api_reference(openapi_url=app.openapi_url, title="Documentation")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


#####################################################################
#####################################################################
#### WE COMMENTED OUT THE CODE BELOW BECAUSE WE ARE USING ROUTER ####
#####################################################################
#####################################################################

# Data is now in data.json and is getting loaded using db.py
# teachers: list[dict] = [
#     {
#         "id": 1,
#         "name": "Anas",
#         "age": 35,
#         "experience_years": 15,
#         "degree": ["BS(CS)", "MS(Cyber)"],
#         "marital_status": "single",
#     },
#     {
#         "id": 2,
#         "name": "Hamza",
#         "age": 24,
#         "experience_years": 2,
#         "degree": ["BS(SE)"],
#         "marital_status": "single",
#     },
#     {
#         "id": 3,
#         "name": "Ayesha",
#         "age": 29,
#         "experience_years": 5,
#         "degree": ["BS(CS)", "MS(DS)"],
#         "marital_status": "divorced",
#     },
#     {
#         "id": 4,
#         "name": "Bilal",
#         "age": 35,
#         "experience_years": 12,
#         "degree": ["BS(IT)", "MS(CS)", "PhD(AI)"],
#         "marital_status": "single",
#     },
#     {
#         "id": 5,
#         "name": "Fatima",
#         "age": 26,
#         "experience_years": 3,
#         "degree": ["BS(CS)", "MS(Cyber)"],
#         "marital_status": "married",
#     },
#     {
#         "id": 6,
#         "name": "Zain",
#         "age": 42,
#         "experience_years": 18,
#         "degree": ["BS(CS)", "MBA"],
#         "marital_status": "in_relationship",
#     },
#     {
#         "id": 7,
#         "name": "Sara",
#         "age": 31,
#         "experience_years": 8,
#         "degree": ["BS(AI)", "MS(AI)"],
#         "marital_status": "divorced",
#     },
#     {
#         "id": 8,
#         "name": "Omar",
#         "age": 23,
#         "experience_years": 1,
#         "degree": ["BS(CS)"],
#         "marital_status": "divorced",
#     },
#     {
#         "id": 9,
#         "name": "Khadija",
#         "age": 28,
#         "experience_years": 4,
#         "degree": ["BS(IT)", "MS(SE)"],
#         "marital_status": "divorced",
#     },
#     {
#         "id": 10,
#         "name": "Ali",
#         "age": 33,
#         "experience_years": 9,
#         "degree": ["BS(SE)", "MS(CS)"],
#         "marital_status": "in_relationship",
#     },
#     {
#         "id": 11,
#         "name": "Mariam",
#         "age": 27,
#         "experience_years": 4,
#         "degree": ["BS(CS)"],
#         "marital_status": "married",
#     },
# ]

# We can create a base model/class using pydantic which will allow fastapi to do the validation according to the model on its own
# class Teacher(BaseModel):
#     name: str
#     age: int
#     experience_years: int
#     degree: list[str]

# Moved it to schemas.py where all the models will be present


# def search_teacher(id: int):
#     for teacher in teachers:
#         if teacher["id"] == id:
#             return teacher
#     return 0


# As we are using path parameters in the next route, we need to define the static route before the dynamic one so that interpreter reads
# the static one without giving the error when both predecessing paths are same
# @app.get("/teachers")
# If we add an argument to the function and that is not a path parimiter, it automatically becomes a query parameter
# which can be accessed like /teachers?sort:asc
# def get_teachers(sort: str | None = None, session: Session = Depends(get_session)):

# We will use annotation to make the Depends statement short hand
# async def get_teachers(session: SessionDep, sort: str | None = None):

    # teacher_names = []

    # teacher_names = db.get_teacher_all()

    # Using session for getting data from Teacher table
    # teacher_names = await session.scalars(select(Teacher)).all()

    # print("teacher names", teacher_names)

    # if sort == "asc":
    #     # sorted_teacher_names = sorted(teacher_names, key= lambda t: t.name)
    #     sorted_teacher_names = await session.scalars(
    #         select(Teacher.name).order_by(asc(Teacher.name))
    #     ).all()
    #     return sorted_teacher_names

    # elif sort == "desc":
    #     sorted_teacher_names = await session.scalars(
    #         select(Teacher.name).order_by(desc(Teacher.name))
    #     ).all()
    #     return sorted_teacher_names

    # else:
    #     return teacher_names


# We can validate response by adding response_model
# @app.get("/teachers/{teacher_id}", response_model=TeacherGet)
# Adding type hinting will automatically manages the validation for dynamic endpoints, as well as for the return types
# async def get_teacher(teacher_id: int, session: SessionDep):
    # teacher = search_teacher(teacher_id)

    # teacher = db.get_teacher(teacher_id)

    # teacher = await session.get(Teacher, teacher_id)

    # if teacher is None:
    #     raise HTTPException(
    #         status_code=404, detail=f"Teacher with id {teacher_id} not found"
    #     )

    # return teacher


# @app.post("/teachers")
# The degree won't get uploaded because when we are posting data like this, we post it using queries,
# and quries don't support lists
# def add_teacher(name: str, age: int, experience_years: int, degree: list[str]):
#     id = max(teachers.keys()) + 1

#     if experience_years >= 5:
#         teachers[id] = {
#             "name": name,
#             "age": age,
#             "experience_years": experience_years,
#             "degree": degree,
#         }
#         return teachers[id]

#     else:
#         raise HTTPException(
#             status_code=400, detail="Teacher experience is less than 5 years"
#         )

# We can also use dict here
# def add_teacher(data: dict):
#     teacher_id = (teachers[len(teachers)-1]["id"]) + 1

#     teachers.append(
#         {
#             "id": teacher_id,
#             "name": data["name"],
#             "age": data["age"],
#             "experience_years": data["experience_years"],
#             "degree": data["degree"],
#         }
#     )

#     return teachers[len(teachers)-1]


# Here we will use the pydantic model to get the data
# @app.post("/teachers")
# def add_teacher(teacher: TeacherAdd, session: SessionDep):
# async def add_teacher(teacher: Teacher, session: SessionDep):
    # teacher_id = (teachers[len(teachers) - 1]["id"]) + 1

    # teachers.append(
    #     {
    #         "id": teacher_id,
    #         "name": teacher.name,
    #         "age": teacher.age,
    #         "experience_years": teacher.experience_years,
    #         "degree": teacher.degree,
    #         "marital_status": teacher.marital_status,
    #     }
    # )
    # save()
    # return teachers[len(teachers) - 1]

    # result = db.add_teacher(
    #     teacher.name,
    #     teacher.age,
    #     teacher.experience_years,
    #     teacher.degree,
    # teacher.marital_status,
    # )

    # return result

    # Adding teacher using session

    # new_teacher = Teacher(
    #     **teacher.model_dump()
    # )

    # session.add(teacher)
    # await session.commit()
    # await session.refresh(teacher)

    # return teacher


# Put method is used to completely replace an entry from the data with the new data
# @app.put("/teachers/{teacher_id}")
# def update_teacher(teacher_id: int, data: dict):
#     teachers[teacher_id] = {
#         "name": data["name"],
#         "age": data["age"],
#         "experience_years": data["experience_years"],
#         "degree": data["degree"]
#     }
#     return teachers[teacher_id]


# We can do it using query parameters as well
# @app.put("/teachers/{teacher_id}", response_model=TeacherUpdate)
# def update_teacher(
#     teacher_id: int, name: str, age: int, experience_years: int, degree: str
# ):
#     for index, teacher in enumerate(teachers):
#         if teacher["id"] == teacher_id:
#             teachers[index] = {
#                 "id": teacher_id,
#                 "name": name,
#                 "age": age,
#                 "experience_years": experience_years,
#                 "degree": degree,
#             }
#             return teachers[index]
#     raise HTTPException(
#         status_code=400, detail=f"Teacher with id {teacher_id} not found"
#     )


# Using pydantic model for updating
# @app.put("/teachers/{teacher_id}", response_model=Teacher)
# async def update_teacher(teacher_id: int, data: TeacherUpdate, session: SessionDep):
    # for index, teacher in enumerate(teachers):
    #     if teacher["id"] == teacher_id:
    #         teacher.update(data.model_dump())
    #         save()
    #         # We need to return teacher separately because it won't work in a single liner
    #         return teacher
    # raise HTTPException(
    #     status_code=404, detail=f"Teacher with id {teacher_id} not found"
    # )

    # db.update_teacher(
    #     teacher_id,
    #     data.name,
    #     data.age,
    #     data.experience_years,
    #     data.degree,
    #     data.marital_status,
    # )

    # return db.get_teacher(teacher_id)
    # db_teacher= await session.get(Teacher, teacher_id)
    # db_teacher.sqlmodel_update(data.model_dump()) # It will take data without ** because it can process pydantic models directly
    # session.add(db_teacher)
    # await session.commit()
    # await session.refresh(db_teacher)

    # return db_teacher


# We use patch method if we want to update only some specific fields, not the whole entry
# @app.patch("/teachers/{teacher_id}", response_model=Teacher)
# async def patch_teacher(teacher_id: int, data: ModelTeacherUpdate, session: SessionDep):
    # if name:
    #     teachers[teacher_id]["name"] = name
    # if age:
    #     teachers[teacher_id]["age"] = age
    # if experience_years:
    #     teachers[teacher_id]["experience_years"] = experience_years
    # if degree:
    #     teachers[teacher_id]["degree"] = degree

    # We can use append method as well instead of using if statements
    # teachers.append(data)
    # return teachers[teacher_id]

    # for index, teacher in enumerate(teachers):
    #     if teacher["id"] == teacher_id:
    #         teachers[index].update(data.model_dump(exclude_unset=True))
    #         save()
    #         return teachers[index]

    # if db.get_teacher(teacher_id) is None:
    #     raise HTTPException(
    #         status_code=404, detail=f"Teacher with id {teacher_id} not found"
    #     )
    # teacher_data = data.model_dump(exclude_unset=True)
    # db.patch_teacher(teacher_id, **teacher_data)
    # return db.get_teacher(teacher_id)

    # db_teacher = await session.get(Teacher, teacher_id)
    # db_teacher.sqlmodel_update(data.model_dump(exclude_unset=True))
    # session.add(db_teacher)
    # await session.commit()
    # await session.refresh(db_teacher)

    # return db_teacher



# @app.delete("/teachers/{teacher_id}", response_model=TeacherDelete)
# async def delete_teacher(teacher_id: int, session: SessionDep):
    # for index, teacher in enumerate(teachers):
    #     if teacher["id"] == teacher_id:
    #         teachers.pop(index)
    #         save()
    #         return {"success": True}
    # raise HTTPException(
    #     status_code=400, detail=f"Teacher with id {teacher_id} not found"
    # # )
    # db_teacher = session.get(Teacher, teacher_id)
    # if db_teacher is None:
    #     raise HTTPException(
    #         status_code=404, detail=f"Teacher with id {teacher_id} not found"
    #     )
    # await session.delete(db_teacher)
    # await session.commit()
    # # result = db.delete_teacher(teacher_id)
    # return {"success": "True"}





##############################################################
##############################################################


# Annotation

# This is how we can annotate a variable
# salary: Annotated[float, "pkr", "usd"]

# # And this is how we can create an annoted data type

# Currency = Annotated[float, "pkr", "usd"]

# foreign_currency: Currency = 100
