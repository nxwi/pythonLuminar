# Program to find the sum of digits of a number input by the user

n = int(input("Enter the number:"))
s = 0

while n != 0:
    r = n % 10
    s += r
    n //= 10
print(s)
