# Write a program to check if a string is a palindrome.

x = input("Enter the string: ")

if x[::] == x[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
