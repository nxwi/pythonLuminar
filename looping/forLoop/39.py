# Program to find the product of digit of the number input by the user

n = int(input("Enter the number:"))

p = 1

for i in range(len(str(n))):
    r = n % 10
    p *= r
    n //= 10
print(p)
