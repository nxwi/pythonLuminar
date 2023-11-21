# write a program to count string without including whitespace

x = input('Enter the string:')

n = 0

for i in x:
    if i.isspace():
        continue
    else:
        n += 1
print(n)
