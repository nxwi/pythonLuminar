# Program to find the product of first n natural numbers

n = int(input("Enter the range:"))

x = 1

for i in range(1, n+1):
    x *= i
print(x)
