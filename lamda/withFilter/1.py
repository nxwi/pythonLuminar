# Program to filter out even numbers from the given list using lambda filter

li = [1, 2, 3, 4]

x = list(filter(lambda i: i % 2 == 0, li))

print(x)
