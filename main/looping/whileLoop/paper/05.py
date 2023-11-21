# Program to print the count of odd numbers between the range input by the user

x = int(input("Enter the start:"))
y = int(input("Enter the end:"))

i = 0

while x <= y:
    if x % 2 == 1:
        i += 1
    x += 1
print(i)
