# create a list of numbers from 1 to 10, take a user input and print its multiples

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = int(input("Enter the number:"))
x = list(map(lambda i: i * n, l))
print(x)
