# Create a program that calculates the factorial of a number.

n = int(input("Enter the number: "))
x = 1

for i in range(1, n + 1):
    x = x * i
print(x)
