# Program to find the product of digits of a number input by the user

n = int(input("Enter the number:"))
p = 1
if n == 0:
    print("0")
else:
    while n != 0:
        r = n % 10
        p *= r
        n //= 10
    print(p)
