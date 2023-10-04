# Program to find factorial of a number input by the user

x = int(input("Enter the number:"))

y = 1

for i in range(1, x+1):
    y *= i
print(y)
