# Program to find sum of digits of a number input by the user

n = int(input("Enter the number:"))

s = 0

for i in range(len(str(n))):
    r = n % 10
    s += r
    n //= 10
print(s)
