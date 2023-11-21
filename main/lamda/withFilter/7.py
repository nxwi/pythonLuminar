# Filter +ve numbers from the given list [1,-1,2,-2,3,-3]

li = [1, -1, 2, -2, 3, -3]

x = list(filter(lambda i: i > 0, li))

print(x)
