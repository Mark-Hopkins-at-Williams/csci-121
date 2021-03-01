def pair(x, y):
    return [x, y]


def append(ls, element):
    if ls == None:
        return pair(element, None)
    while ls[1] != None:
        ls = ls[1]
    ls[1] = pair(element, None)
