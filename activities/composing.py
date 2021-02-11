"""All three of these functions are correct solutions!"""

def compose(f, g):
    return lambda x: f(g(x))

def compose2(f, g):
    func = lambda x: f(g(x))
    return func

def compose3(f, g):
    def func(x):
        return f(g(x))
    return func
