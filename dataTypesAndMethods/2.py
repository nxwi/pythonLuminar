# Program to remove space character from a string input by the user

x = input('Enter the string:')

for i in x:
    if i != ' ':
        print(i, end='')
