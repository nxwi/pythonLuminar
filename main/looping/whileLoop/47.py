# Write a program to enter the numbers till the user enter 0 and at the end it should display the count of positive and
# negative values entered

p = 0
n = 0
i = 1

while i != 0:
    i = int(input("Enter a number:"))
    if i > 0:
        p += 1
    elif i < 0:
        n += 1

print("Number of +ve no=", p)
print("Number of -ve no=", n)
