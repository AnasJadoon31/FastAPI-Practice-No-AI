from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from typing import Any

app = FastAPI()

class_id = 0

teachers = {
    {
    1: {
        "name": "Anas",
        "age": 35,
        "experience_years": 15,
        "degree": ["BS(CS)", "MS(Cyber)"]
    },
    2: {
        "name": "Hamza",
        "age": 24,
        "experience_years": 2,
        "degree": ["BS(SE)"]
    },
    3: {
        "name": "Ayesha",
        "age": 29,
        "experience_years": 5,
        "degree": ["BS(CS)", "MS(DS)"]
    },
    4: {
        "name": "Bilal",
        "age": 35,
        "experience_years": 12,
        "degree": ["BS(IT)", "MS(CS)", "PhD(AI)"]
    },
    5: {
        "name": "Fatima",
        "age": 26,
        "experience_years": 3,
        "degree": ["BS(CS)", "MS(Cyber)"]
    },
    6: {
        "name": "Zain",
        "age": 42,
        "experience_years": 18,
        "degree": ["BS(CS)", "MBA"]
    },
    7: {
        "name": "Sara",
        "age": 31,
        "experience_years": 8,
        "degree": ["BS(AI)", "MS(AI)"]
    },
    8: {
        "name": "Omar",
        "age": 23,
        "experience_years": 1,
        "degree": ["BS(CS)"]
    },
    9: {
        "name": "Khadija",
        "age": 28,
        "experience_years": 4,
        "degree": ["BS(IT)", "MS(SE)"]
    },
    10: {
        "name": "Ali",
        "age": 33,
        "experience_years": 9,
        "degree": ["BS(SE)", "MS(CS)"]
    },
    11: {
        "name": "Mariam",
        "age": 27,
        "experience_years": 4,
        "degree": ["BS(CS)"]
    }
}
}

# As we are using path parameters in the next route, we need to define the static route before the dynamic one so that interpreter reads
# the static one without giving the error when both predecessing paths are same
@app.get("/teachers/all")
def get_teachers():
    return teachers

@app.get("/teachers/{teacher_id}")
# Adding type hinting will automatically manages the validation for dynamic endpoints, as well as for the return types
def get_teacher(teacher_id: int) -> dict[str, Any]:
    # We are using global because python doesn't allow to modify the global variables without global keyword
    global class_id
    class_id += 1
    return {
        "id": teacher_id,
        "name": "Dr. Raheel Siddiqui",
        "designation": "Associate Professor",
        "age": "45",
        "weekly_classes": {
            "Monday": [
                {
                    "class_id": class_id,
                    "time_24_hrs": "09:30",
                    "duration_hrs": "2",
                    "subject": "DSA",
                    "class": "BS(CS) 4-B",
                    "room": "E-209",
                },
                {
                    "class_id": class_id,
                    "time_24_hrs": "11:30",
                    "duration_hrs": "2",
                    "subject": "DSA",
                    "class": "BS(CS) 4-B",
                    "room": "E-209",
                },
            ],
            "Tuesday": [
                {
                    "class_id": class_id,
                    "time_24_hrs": "09:30",
                    "duration_hrs": "2",
                    "subject": "DSA",
                    "class": "BS(CS) 4-B",
                    "room": "E-209",
                }
            ],
            "Wednesday": [
                {
                    "class_id": class_id,
                    "time_24_hrs": "09:30",
                    "duration_hrs": "2",
                    "subject": "DSA",
                    "class": "BS(CS) 4-B",
                    "room": "E-209",
                }
            ],
        },
    }


@app.get("/scalar")
def get_scalar():
    return get_scalar_api_reference(openapi_url=app.openapi_url, title="Documentation")
