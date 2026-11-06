import statistics
from typing import TypedDict


class Student(TypedDict):
    name: str
    score: float


# Python 3.12+ type alias statement (PEP 695)
type StudentList = list[Student]

students: StudentList = [
    {"name": "James", "score": 45},
    {"name": "Deborah", "score": 82},
    {"name": "Chinedu", "score": 67},
    {"name": "Aisha", "score": 91},
    {"name": "Tunde", "score": 58},
]


def validate_student(name: str, score: float) -> Student:
    # Adaptive maintenance: new validation feature (standard library only)
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Student name must be a non-empty string")
    if isinstance(score, bool) or not isinstance(score, (int, float)):
        raise TypeError("Score must be a number")
    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100")
    return {"name": name.strip(), "score": score}


def average_score(data: StudentList) -> float:
    if len(data) == 0:
        return 0  # Corrective maintenance: avoid ZeroDivisionError on an empty list
    total = 0
    for d in data:
        total += d["score"]
    return total / len(data)


def median_score(data: StudentList) -> float:
    # Perfective maintenance: extra statistic
    if not data:
        return 0
    return statistics.median(d["score"] for d in data)


def add_student(name: str, score: float) -> None:
    students.append(validate_student(name, score))


def get_students() -> StudentList:
    return students
