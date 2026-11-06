"""Reusable helper functions that work on any list of student records."""


def highest_score(data):
    """Return the student with the highest score, or None if the list is empty."""
    if not data:
        return None
    return max(data, key=lambda d: d["score"])


def lowest_score(data):
    """Return the student with the lowest score, or None if the list is empty."""
    if not data:
        return None
    return min(data, key=lambda d: d["score"])


def pass_count(data, pass_mark=50):
    """Return how many students scored at least ``pass_mark``."""
    return sum(1 for d in data if d["score"] >= pass_mark)
