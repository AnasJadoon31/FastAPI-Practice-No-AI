from enum import Enum
from typing import Optional
# from random import randint

from pydantic import BaseModel, Field, create_model


# We can create enums if we want the string to be any of the specified value, not other than that
class Enum_Marital_Status(str, Enum):
    single = "single"
    in_relationship = "in_relationship"
    married = "married"
    divorced = "divorced"


# We can use Field() to add validation
# class Teacher(BaseModel):
#     name: str = Field(description="Name for teacher", max_length=50, min_length=3)
#     age: int = Field(description="Age must be less than or equal to 65", le=65)
#     experience_years: int = Field(
#         description="Experience Years must be less than or equal to 5", le=5
#     )
#     degree: list[str] | None = Field(description="Degrees are optional", default=None)
#     # Using Enum here and making it default to None because our data doesn't contain it, and pydantic is strict about validation
#     marital_status: Enum_Marital_Status | None = Field(default=None)


# We make different models for each method while following industry standards


class BaseTeacher(BaseModel):
    name: str = Field(description="Name for teacher", max_length=50, min_length=3)
    age: int = Field(description="Age must be less than or equal to 65", le=65)
    experience_years: int = Field(
        description="Experience Years must be less than or equal to 5", ge=5
    )
    degree: list[str] = Field(description="Degree List")
    marital_status: Enum_Marital_Status = Field(
        description="Marital Status of the teacher"
    )


class TeacherAdd(BaseTeacher):
    pass


class TeacherGet(BaseTeacher):
    id: int


class TeacherUpdate(BaseTeacher):
    pass


class TeacherDelete(BaseModel):
    success: bool


class TeacherPatch(BaseModel):
    name: str | None = Field(
        description="Name for teacher", max_length=50, min_length=3, default=None
    )
    age: int | None = Field(
        description="Age must be less than or equal to 65", le=65, default=None
    )
    experience_years: int | None = Field(
        description="Experience Years must be less than or equal to 5",
        ge=5,
        default=None,
    )
    degree: list[str] | None = Field(description="Degree List", default=None)
    marital_status: Enum_Marital_Status | None = Field(
        description="Marital Status of the teacher", default=None
    )


# reg_num: int = 0


# def generate_registration():
#     global reg_num
#     reg_num += 1
#     return reg_num


# class Student(BaseModel):
#     # We can generate random numbers as well
#     # Add description check to add description in the documentation
#     enrollment: int = Field(
#         description="Enrollment for student", default=randint(0, 1000)
#     )
#     # or run a function and get the value it returned
#     registration: int = Field(default_factory=generate_registration)
