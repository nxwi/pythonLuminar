# Program to print the total count of uppercase and lowercase letters in a string input by the user

x = input('Enter the string:')

u = 0
l = 0

for i in x:
    if i.isupper():
        u += 1
    elif i.islower():
        l += 1
print("No. of uppercase:", u)
print("No. of lowercase:", l)
