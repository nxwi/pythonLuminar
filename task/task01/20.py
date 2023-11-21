# Create a program to check if a given year is a leap year.

year = int(input("Enter the year:"))

if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        print(year, "is not a leap year.")
    else:
        print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
