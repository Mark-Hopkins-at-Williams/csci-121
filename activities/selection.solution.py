def selection_sort(ls):
    for back in range(0, len(ls)):
        selection = back
        for student in range(back, len(ls)):
            if ls[student] < ls[selection]:
                selection = student
        ls[back], ls[selection] = ls[selection], ls[back]


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

