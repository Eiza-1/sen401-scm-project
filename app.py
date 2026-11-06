"""Demo application for the Student Score Tracker (v1.1).

Run with:  python app.py
"""

from students import (PASS_MARK, add_student, average_score, get_students,
                      median_score, pass_rate)
from utils.helpers import highest_score, lowest_score, pass_count

WIDTH = 34
LINE = "-" * WIDTH


def print_header() -> None:
    """Print the application title banner."""
    print("=" * WIDTH)
    print("   Student Score Tracker v1.1")
    print("=" * WIDTH)


def print_student_table(data) -> None:
    """Print every student in an aligned table with a PASS/FAIL result."""
    print(f"{'No.':<4}{'Name':<15}{'Score':>6}  Result")
    print(LINE)
    for i, s in enumerate(data, start=1):
        result = "PASS" if s["score"] >= PASS_MARK else "FAIL"
        print(f"{i:<4}{s['name']:<15}{s['score']:>6}  {result}")
    print(LINE)


def print_summary(data) -> None:
    """Print summary statistics for the given students."""
    total = len(data)
    top = highest_score(data)
    low = lowest_score(data)

    print("Summary")
    print(LINE)
    print(f"{'Total Students:':<22}{total}")
    print(f"{'Average Score:':<22}{average_score(data):.2f}")
    print(f"{'Median Score:':<22}{median_score(data):.2f}")
    if top and low:  # both are None when the list is empty
        print(f"{'Highest Score:':<22}{top['name']} ({top['score']})")
        print(f"{'Lowest Score:':<22}{low['name']} ({low['score']})")
    print(f"{f'Passed (>={PASS_MARK}):':<22}{pass_count(data, PASS_MARK)} of {total}")
    print(f"{'Pass Rate:':<22}{pass_rate(data):.1f}%")
    print(LINE)


def main() -> None:
    """Show the students, add a new one, then print the summary."""
    print_header()
    print_student_table(get_students())

    new = add_student("Ngozi", 74)
    print(f"Added new student: {new['name']} ({new['score']})")
    print()

    print_summary(get_students())


if __name__ == "__main__":
    main()
