# Program to check a number is +ve, +ve or zero

x = int(input("Enter the number:"))

if x == 0:
    print("It is zero.")
elif x > 0:
    print(x, "is a positive number.")
else:
    print(x, "is a negative number.")
