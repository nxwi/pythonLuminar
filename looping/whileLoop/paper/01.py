# program to find factorial of a number using while loop

x = int(input("Enter the number:"))

y = 1

while x > 0:
    y *= x
    x -= 1
print(y)
