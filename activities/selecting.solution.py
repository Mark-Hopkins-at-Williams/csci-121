def selection_sort(ls):
    counter = 0
    for position in range(0, len(ls)):
        selection = position
        for student in range(position + 1, len(ls)):
            counter += 1
            if ls[student] < ls[selection]:
                selection = student
        ls[position], ls[selection] = ls[selection], ls[position]
    return counter


def bubble_sort(ls):
    counter = 0
    for goal in range(len(ls), 0, -1):
        for baton in range(0, goal - 1):
            counter += 1
            if ls[baton + 1] < ls[baton]:
                ls[baton], ls[baton + 1] = ls[baton + 1], ls[baton]
    return counter


def insertion_sort(ls):
    counter = 0
    for kid in range(0, len(ls)):
        for teacher in range(kid, 0, -1):
            counter += 1
            if ls[teacher] < ls[teacher - 1]:
                ls[teacher], ls[teacher - 1] = ls[teacher - 1], ls[teacher]
    return counter

