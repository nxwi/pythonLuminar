# Take three string from the user and return the largest string

a = input('Enter the first string:')
b = input('Enter the second string:')
c = input('Enter the third string:')

x = len(a)
y = len(b)
z = len(c)
if x == y == z:
    print("All are equal")
else:
    if x > y and x > z:
        print(a, 'is the largest string')
    elif y > x and y > z:
        print(b, 'is the largest string')
    elif z > x and z > y:
        print(c, 'is the largest string')
