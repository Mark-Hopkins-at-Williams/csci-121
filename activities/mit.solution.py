def multiply(x, y):
    """ Assuming positive integers x and y... """
    if y == 1:
        return x
    else:
        return x + multiply(x, y-1)


def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp-1)


def countdown(n):
    if n >= 0:
        print(n)
        countdown(n-1)


def countup(n):
    if n >= 0:
        countup(n-1)
        print(n)


def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse(s[:-1])


def indivisible_by_2_up_to(n, factor):
    if factor <= 1:
        return True
    else:
        divisible_by_factor = (n % factor == 0)
        return ((not divisible_by_factor) and
                indivisible_by_2_up_to(n, factor - 1))


def is_prime(n):
    if n == 1:
        return False
    else:
        return indivisible_by_2_up_to(n, n-1)


def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
