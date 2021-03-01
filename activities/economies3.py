def pair(x, y):
    return [x, y]


def insert(ls, element, position):
    for _ in range(0, position):
        ls = ls[1]
    inserted = pair(element, ls[1])
    ls[1] = inserted
