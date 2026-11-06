"""Student data module for the Student Score Tracker.

Holds the in-memory list of students and the functions that read, validate
and summarise it. Version 1.1 - see README.md for the maintenance history.
"""

import statistics
from typing import TypedDict

# --- Configuration constants (one place to change rules) -------------------
PASS_MARK = 50
MIN_SCORE = 0
MAX_SCORE = 100


class Student(TypedDict):
    """A single student record."""

    name: str
    score: float


# Python 3.12+ type alias statement (PEP 695)
type StudentList = list[Student]

# --- Data -------------------------------------------------------------------
students: StudentList = [
    {"name": "James", "score": 45},
    {"name": "Deborah", "score": 82},
    {"name": "Chinedu", "score": 67},
    {"name": "Aisha", "score": 91},
    {"name": "Tunde", "score": 58},
]


# --- Validation ---------------------------------------------------------------
def validate_student(name: str, score: float) -> Student:
    """Check a name and score and return a clean Student record.

    Args:
        name: The student's name; must contain at least one non-space character.
        score: A number between MIN_SCORE and MAX_SCORE inclusive.

    Returns:
        A Student dictionary with the name stripped of surrounding spaces.

    Raises:
        ValueError: If the name is empty or the score is out of range.
        TypeError: If the score is not a number.
    """
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Student name must be a non-empty string")
    # bool is a subclass of int, so reject it explicitly
    if isinstance(score, bool) or not isinstance(score, (int, float)):
        raise TypeError("Score must be a number")
    if not MIN_SCORE <= score <= MAX_SCORE:
        raise ValueError(f"Score must be between {MIN_SCORE} and {MAX_SCORE}")
    return {"name": name.strip(), "score": score}


# --- Statistics ---------------------------------------------------------------
def _scores(data: StudentList) -> list[float]:
    """Return just the scores from a list of students (shared helper, DRY)."""
    return [d["score"] for d in data]


def average_score(data: StudentList) -> float:
    """Return the mean score, or 0 for an empty list (avoids ZeroDivisionError)."""
    if not data:
        return 0
    return statistics.fmean(_scores(data))


def median_score(data: StudentList) -> float:
    """Return the median score, or 0 for an empty list."""
    if not data:
        return 0
    return statistics.median(_scores(data))


def pass_rate(data: StudentList, pass_mark: float = PASS_MARK) -> float:
    """Return the percentage of students scoring at least ``pass_mark``."""
    if not data:
        return 0.0
    passed = sum(1 for s in _scores(data) if s >= pass_mark)
    return passed / len(data) * 100


# --- Data access -------------------------------------------------------------
def add_student(name: str, score: float) -> Student:
    """Validate and append a new student, returning the stored record."""
    record = validate_student(name, score)
    students.append(record)
    return record


def get_students() -> StudentList:
    """Return a copy of the student list so callers cannot modify it by accident."""
    return list(students)
