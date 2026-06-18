from typing import Any
# It can be changed afterwards
changable_variable = "Anything"
changable_variable = "Nothing"

# ---------------------------

# To define a type we can do:
defined_variable: int = (
    1  # We cannot change it to string later on (Use mypy extension for error handling)
)
# defined_variable = "Anas" # Will give error

# ---------------------------

# Piping, to support multiple values in a variable
piped_variable: int | str = "Anas"
piped_variable = 31

# ---------------------------

# Variable that can have no value

not_initialized: None

# ---------------------------

# Variable not initialized yet, but has a data type

not_initialized_but_with_data_type: int
not_initialized_but_with_data_type = 5

# ---------------------------
# ---------------------------
# ---------------------------
# Functions


def power(num: int | float, exp: int | float = 2) -> int | float:
    return pow(num, exp)


# The arrow after function tells that the returned value will either be int or float

power_2 = power(2)

# ---------------------------
# ---------------------------
# ---------------------------
# List, tuple, and dictionary

# Lists

# This list can have any data type
anything: list = ["apple", "banana", "mango", 12, 13.1]

# This list can only have strings
string_only: list[str] = ["apple", "banana", "mango"]

# This list can have both, strings and integers
string_and_int: list[str | int] = ["apple", "banana", "mango", 1122]


# ---------------------------

# Tuples (immutable/can't be modified later)

# Tuple which can hold anything
tup: tuple = (1, 3, 5, "Banana")

# Tuple which can only hold one value of one data type

tup_specific: tuple[str] = (
    "Anas",
)  # Comma is necessary as it tells python that it is tuple, otherwise it would be treated as an expression

# Tuple that can hold many values of one data type

tup_specific_many: tuple[str, ...] = ("Anas", "Amaan", "Hamza")

# Tuple that can hold fixed values

tup_fixed: tuple[str, int, float] = ("Karachi", 31, 3.58) # It will only have 3 values of defined data types


# ---------------------------

# Dictionary

country_capitals: dict[str, str] = {
    "Pakistan": "Karachi"
}

teacher_details: dict[str, int | str] = {
    "Id": 1,
    "Name": "John Doe"
}

# Using any data type, first we need to import Any from typing

teacher_details_any: dict[str, Any] = {
    "Name": "John Doe",
    "Age": 31,
    "CGPA": 3.96
}

#--------------------------

# Using classes to make data types

class Airplane:
    def __init__(self, name: str, capacity: int, color: str, model: str):
        self.name = name,
        self.capacity = capacity,
        self.color = color,
        self.model = model


airplane = Airplane("Airbus 320", 180, "white", "A320")

airplane_fares: tuple[Airplane, float | int] = (airplane, 4520.31)


