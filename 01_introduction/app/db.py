import json


teachers: list = []

with open("FastAPI-Practice-No-AI/01_introduction/app/data.json") as json_file:
    data = json.load(json_file)
    teachers = data

print (teachers)


def save():
    with open("FastAPI-Practice-No-AI/01_introduction/app/data.json", "w") as json_file:
        json.dump(teachers, json_file)