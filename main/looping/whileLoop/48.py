# Write a program to enter the numbers till the user enter 0 or negative value and at the end it should display the
# count of positive and negative values entered

even = 0
odd = 0
i = 1

while i > 0:
    i = int(input("Enter a number:"))
    if i % 2 == 0 and i > 0:
        even += 1
    elif i % 2 == 1 and i > 0:
        odd += 1

print("Number of odd no=", odd)
print("Number of even no=", even)
