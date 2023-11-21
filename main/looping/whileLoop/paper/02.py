# Program to print odd numbers between the range input by the user

x = int(input("Enter the start:"))
y = int(input("Enter the end:"))

while x <= y:
    if x % 2 == 1:
        print(x)
    x += 1
