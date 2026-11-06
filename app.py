from students import students, average_score, add_student
from utils.helpers import highest_score, lowest_score, pass_count


def main():
    print("=== Student Score Tracker v1.0 ===")
    print()

    print("Current Students:")
    for s in students:
        print(s["name"], "-", s["score"])
    print()

    add_student("Ngozi", 74)
    print("Added new student: Ngozi (74)")
    print()

    top = highest_score(students)
    low = lowest_score(students)

    print("Total Students:", len(students))
    print("Average Score:", average_score(students))
    print("Highest Score:", top["name"], top["score"])
    print("Lowest Score:", low["name"], low["score"])
    print("Students Passed (>=50):", pass_count(students))


if __name__ == "__main__":
    main()
