def add(a, b):
    return a + b


def area_of_circle(r):
    from math import pi
    return pi * r * r


def rev_num(n):
    i = str(n)
    return int(i[::-1])


def product(li):
    from functools import reduce
    return reduce(lambda i, j: i * j, li)


def smallest(li):
    from functools import reduce
    # return reduce(lambda i, j: i if i < j else j,, li)
    return reduce(min, li)
