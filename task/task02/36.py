# Create a program to check if a string contains only alphabetic characters.

string = input("Enter a string: ")

if string.isalpha():
    print(string, "is an alphabetic string")
else:
    print(string, "is not an alphabetic string")
