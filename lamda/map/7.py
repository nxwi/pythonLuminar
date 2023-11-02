# Create a function using def and pass two list into the function, and using lambda map find the product of the
# list and return a new list

def product(x, y):
    return list(map(lambda i, j: i * j, x, y))


l1 = [1, 2, 3, 4, 5, 6]
l2 = [1, 2, 3, 4, 5]

print(product(l1, l2))
