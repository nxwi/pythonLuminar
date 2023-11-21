# Write a program to check if a given string contains only digits.

string = input("Enter the string: ")

is_digit = True
for char in string:
    if not char.isdigit():
        is_digit = False
        break

if is_digit:
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")
