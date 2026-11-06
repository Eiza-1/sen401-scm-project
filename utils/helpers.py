def highest_score(data):
    if not data:
        return None  # Corrective maintenance: avoid IndexError on an empty list
    best = data[0]
    for d in data:
        if d["score"] > best["score"]:
            best = d
    return best


def lowest_score(data):
    if not data:
        return None  # Corrective maintenance: avoid IndexError on an empty list
    worst = data[0]
    for d in data:
        if d["score"] < worst["score"]:
            worst = d
    return worst


def pass_count(data, pass_mark=50):
    count = 0
    for d in data:
        if d["score"] >= pass_mark:
            count += 1
    return count
