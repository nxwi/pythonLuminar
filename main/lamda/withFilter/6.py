# Filter odd numbers from the given list [1,2,3,4,5,6]

li = [1, 2, 3, 4, 5, 6]

x = list(filter(lambda i: i % 2 == 1, li))

print(x)
