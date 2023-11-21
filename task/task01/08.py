# Create a Python program to print the multiplication table of a given number.

n = int(input("Enter the number: "))

for i in range(1, 11):
    print(i, "*", n, "=", i * n)
