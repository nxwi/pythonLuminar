# Program to check a number is odd or even

x = int(input("Enter the the number:"))

if x == 0:
    print(x, "is not odd or even number.")
elif x % 2 == 0:
    print(x, "is an even number.")
else:
    print(x, "is an odd number.")
