from students import students, average_score, median_score, add_student
from utils.helpers import highest_score, lowest_score, pass_count

PASS_MARK = 50
LINE = "-" * 34


def main():
    print("=" * 34)
    print("   Student Score Tracker v1.1")
    print("=" * 34)

    print(f"{'No.':<4}{'Name':<15}{'Score':>6}  Result")
    print(LINE)
    for i, s in enumerate(students, start=1):
        result = "PASS" if s["score"] >= PASS_MARK else "FAIL"
        print(f"{i:<4}{s['name']:<15}{s['score']:>6}  {result}")
    print(LINE)

    add_student("Ngozi", 74)
    print("Added new student: Ngozi (74)")
    print()

    top = highest_score(students)
    low = lowest_score(students)
    passed = pass_count(students, PASS_MARK)
    total = len(students)

    print("Summary")
    print(LINE)
    print(f"{'Total Students:':<22}{total}")
    print(f"{'Average Score:':<22}{average_score(students):.2f}")
    print(f"{'Median Score:':<22}{median_score(students):.2f}")
    if top and low:
        print(f"{'Highest Score:':<22}{top['name']} ({top['score']})")
        print(f"{'Lowest Score:':<22}{low['name']} ({low['score']})")
    print(f"{f'Passed (>={PASS_MARK}):':<22}{passed} of {total}")
    print(f"{'Pass Rate:':<22}{(passed / total * 100) if total else 0:.1f}%")
    print(LINE)


if __name__ == "__main__":
    main()
