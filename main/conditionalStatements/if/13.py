# program to check a number input by the user is divisible by both two and three

x = int(input("Enter the number:"))

if x % 2 == 0 & x % 3 == 0:
    print(x, "is divisible by 2 and 3.")
else:
    print(x, "is not divisible by 2 and 3.")
