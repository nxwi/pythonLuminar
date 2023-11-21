# Create a program to swap the values of two variables.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# a, b = b, a

a = a + b
b = a - b
a = a - b

print(a, b)
