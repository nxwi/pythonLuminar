# Find the minimum,maximum and product of a list

from functools import reduce

li = [100, 200, 300, 400, 500]

# minimum
print(reduce(lambda i, j: i if i < j else j, li))
print(reduce(min, li))

# maximum

print(reduce(lambda i, j: i if i >= j else j, li))
print(reduce(max, li))

# product

print(reduce(lambda i, j: i * j, li))
