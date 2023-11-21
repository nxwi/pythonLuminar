# Program to remove duplicate elements from a string input by the user

x = input('Enter the string:')

s = ''

for i in x:
    if i not in s:
        s += i
print(s)
