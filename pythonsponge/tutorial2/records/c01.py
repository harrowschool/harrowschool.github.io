from collections import namedtuple
from enum import Enum

class Yeargroups(Enum):
    Y7 = "Year 7"
    Y8 = "Year 8"
    Y9 = "Year 9"

Student = namedtuple("Student", "name age year")

def listStudents(students):
    for s in students:
        print(f"{s.name} is {s.age} years and is in {s.year.value}")

students = [
    Student("Trevor", 11, Yeargroups.Y7),
    Student("Kailani", 12, Yeargroups.Y8)
]

listStudents(students)

# But changing Trevor's age would involve making a new tuple!
name, age, year = students[0]
students[0] = Student(name, age + 1, year)

print("After Trevor's birthday:")

listStudents(students)