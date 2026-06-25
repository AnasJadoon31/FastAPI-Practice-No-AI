# import json


# teachers: list = []

# with open("FastAPI-Practice-No-AI/01_introduction/app/data.json") as json_file:
#     data = json.load(json_file)
#     teachers = data

# print (teachers)


# def save():
#     with open("FastAPI-Practice-No-AI/01_introduction/app/data.json", "w") as json_file:
#         json.dump(teachers, json_file)

#############################3

# Now we will use SQLite instead of raw json because it is more reliable

# import sqlite3
# import json

# teachers: list = []
# with open("FastAPI-Practice-No-AI/01_introduction/app/data.json") as json_file:
# data = json.load(json_file)
# teachers = data

# for teacher in teachers:
# teacher["degree"] = json.dumps(teacher["degree"])

# Create a connection with sqlite db. If file won't be present, it will create one
# connection = sqlite3.Connection("sqlite.db")

# We will write queries through cursor
# cursor = connection.cursor()

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS Teacher (
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     age INTEGER,
#     experience_years INTEGER,
#     degree TEXT
#     )
# """)

# cursor.execute("DROP TABLE Teacher")
# connection.commit()
# If we do like this, we would need our data to be converted into tuple because ? requires the exact data
# cursor_insert_query = ('''
#     INSERT INTO Teacher (id, name, age, experience_years, degree)
#     VALUES (?, ?, ?, ?, ?)
# ''')

# We can overcom this by replacing question marks with the keys in our dictionary
# cursor_insert_query = ('''
#     INSERT INTO Teacher (id, name, age, experience_years, degree)
#     VALUES (:id, :name, :age, :experience_years, :degree)
# ''')

# cursor.executemany(cursor_insert_query, teachers)


# To fetch the data, we need to do this:

# cursor.execute("""
#     SELECT * FROM Teacher
#     WHERE name LIKE "A%"
# """)

# To fetch all
# result = cursor.fetchall()

# To fetch many (first five)
# result = cursor.fetchmany(5)

# To fetch the first one
# result = cursor.fetchone()


# print (result)

# To make changes to data, we need to commit as well, we do it like this:
# connection.commit()

# connection.close()


##########################################################################
##########################################################################
# Now we need to create the Database object which we would be able to add teacher, update teacher, delete teacher and get teacher
import sqlite3
from typing import Any
import json

teachers: list = []
with open("FastAPI-Practice-No-AI/01_introduction/app/data.json") as json_file:
    data = json.load(json_file)
    teachers = data

for teacher in teachers:
    teacher["degree"] = json.dumps(teacher["degree"])


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("database.db", check_same_thread=False)
        # This is required to get the keys as well in the response
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()

        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS Teacher(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            experience_years INTEGER,
            degree TEXT,
            marital_status TEXT             
            )
        """)

        self.cur.execute("SELECT COUNT(*) FROM Teacher")
        row_count = self.cur.fetchone()[0]

        if row_count == 0:
            print("Adding test data...")
            self.add_teachers_from_data()

        else:
            print("Data already present, booting up the system...")

    def add_teachers_from_data(self):
        len(teachers)
        insert_query = """
            INSERT INTO Teacher (
                name,
                age,
                degree,
                experience_years,
                marital_status        
            )
            VALUES (
                :name,
                :age,
                :degree,
                :experience_years,
                :marital_status
            )
        """

        self.cur.executemany(insert_query, teachers)

        self.conn.commit()

    def add_teacher(
        self,
        name: str,
        age: int,
        experience_years: int,
        degree: list[str],
        marital_status: str,
    ):
        self.cur.execute("SELECT MAX(id) FROM Teacher")
        result = self.cur.fetchone()
        if result is not None:
            teacher_id = result[0] + 1
        else:
            teacher_id = 1

        self.cur.execute(
            """
            INSERT INTO Teacher (name, age, experience_years, degree, marital_status)
            VALUES (
            :name, 
            :age, 
            :experience_years, 
            :degree,
            :marital_status)
    """,
            {
                "name": name,
                "age": age,
                "experience_years": experience_years,
                "degree": json.dumps(degree),
                "marital_status": marital_status,
            },
        )
        self.conn.commit()

        return self.get_teacher(teacher_id)

    def get_teacher_all(self):
        self.cur.execute("SELECT * FROM Teacher")
        rows = self.cur.fetchall()
        dict_result = [dict(result) for result in rows]

        for teacher in dict_result:
            if teacher["degree"]:
                teacher["degree"] = json.loads(teacher["degree"])
        return dict_result

    def get_teacher(self, id: int):
        self.cur.execute("SELECT * FROM Teacher WHERE id = :id", {"id": id})
        row = self.cur.fetchone()
        if row is None:
            return None
        dict_result = dict(row)
        dict_result["degree"] = json.loads(dict_result["degree"])
        return dict_result

    def update_teacher(
        self,
        id: int,
        name: str,
        age: int,
        experience_years: int,
        degree: list[str],
        marital_status: str,
    ):
        self.cur.execute(
            """
            UPDATE Teacher SET 
            name = :name, age = :age, 
            experience_years = :experience_years, 
            degree = :degree, 
            marital_status = :marital_status
            WHERE ID = :id
    """,
            {
                "id": id,
                "name": name,
                "age": age,
                "experience_years": experience_years,
                "degree": json.dumps(degree),
                "marital_status": marital_status,
            },
        )
        self.conn.commit()

        return self.get_teacher(id)

    def patch_teacher(
        self,
        id: int,
        name: str | None = None,
        age: int | None = None,
        experience_years: int | None = None,
        degree: list[str] | None = None,
        marital_status: str | None = None,
    ):
        data: dict[str, Any] = {}

        if name is not None:
            data["name"] = name
        if age is not None:
            data["age"] = age
        # We are doing is not None because false will return zero if we use if
        if experience_years is not None:
            data["experience_years"] = experience_years
        if degree is not None:
            data["degree"] = json.dumps(degree)
        if marital_status is not None:
            data["marital_status"] = marital_status

        set_clauses: list = [f"{column} = :{column}" for column in data.keys()]
        set_data: str = ", ".join(set_clauses)
        data["id"] = id

        self.cur.execute(f"UPDATE Teacher SET {set_data} WHERE id = :id", data)
        self.conn.commit()

        return self.get_teacher(id)

    def delete_teacher(self, id: int):
        self.cur.execute("DELETE FROM Teacher WHERE id = :id", {"id": id})
        self.conn.commit()
        return True

    def close(self):
        self.conn.close()
