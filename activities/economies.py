def pair(x, y):
    return [x, y]


def one_element_list(x):
    return pair(x, None)


def three_element_list(x, y, z):
    return pair(x, pair(y, pair(z, None)))


def lprint(ls):
    result = "["
    while ls != None:
        result = result + str(ls[0]) + ", "
        ls = ls[1]
    result = result[:-2] + "]"
    print(result)


def prepend(ls, element):
    """ Fill in with your solution to Economies of Scale (Part 1). """


def append(ls, element):
    """ Fill in with your solution to Economies of Scale (Part 2). """


def insert(ls, element, position):
    """ Fill in with your solution to Economies of Scale (Part 3). """

