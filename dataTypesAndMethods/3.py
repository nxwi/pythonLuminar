# Program to check  a string input by the user is palindrome or not

x = input('Enter the string:')

if x == x[::-1]:
    print(x, 'is palindrome')
else:
    print(x, 'is not palindrome')
