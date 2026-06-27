from sqlmodel import Field
from sqlmodel import SQLModel
from enum import Enum


# We can create enums if we want the string to be any of the specified value, not other than that
class Enum_Marital_Status(str, Enum):
    single = "single"
    in_relationship = "in_relationship"
    married = "married"
    divorced = "divorced"


# SQLModel is used to define a table inside the sql, and is helpful for inserting and fetching data from it as well
class Teacher(SQLModel):
    # Table name will be the class name in lowercase by default and can be modified as below
    __tablename__ = "teacher"

    name: str = Field(description="Name for teacher", max_length=50, min_length=3)
    age: int = Field(description="Age must be less than or equal to 65", le=65)
    experience_years: int = Field(
        description="Experience Years must be greater than or equal to 5", ge=5
    )
    # degree: list[str] = Field(description="Degree List")
    degree: list[str] = Field(description="Degree List")
    marital_status: Enum_Marital_Status = Field(
        description="Marital Status of the teacher"
    )
