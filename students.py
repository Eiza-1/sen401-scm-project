students = [
    {"name": "James", "score": 45},
    {"name": "Deborah", "score": 82},
    {"name": "Chinedu", "score": 67},
    {"name": "Aisha", "score": 91},
    {"name": "Tunde", "score": 58},
]


def average_score(data):
    total = 0
    for d in data:
        total += d["score"]
    return total / len(data)


def add_student(name, score):
    students.append({"name": name, "score": score})


def get_students():
    return students
