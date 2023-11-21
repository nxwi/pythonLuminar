# program to print the last digit of a number is divisible by 3 or not

x = int(input("Enter a number:"))

if (x % 10) % 3 == 0:
    print("Last digit of", x, "is divisible by 3")
else:
    print("Last digit of", x, "is not divisible by 3")
