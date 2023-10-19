# Program to find the string is palindrome or not

x = input('Enter the string:')

rev = ''

for i in range(len(x)-1, -1, -1):
    rev += x[i]
if x == rev:
    print('Palindrome')
else:
    print('Not palindrome')
