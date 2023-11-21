# Program to find the sum of the given list using lambda reduce

from functools import reduce


li = [1, 2, 3, 4, 5, 6]
print(reduce(lambda i, j: i + j, li))
