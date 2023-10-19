# Input a string from the user and only print the elements with even index value

x = input('Enter the string:')

for i in range(0, len(x), 2):
    print(x[i], end='')

for i in x[::2]:
    print(i, end='')
