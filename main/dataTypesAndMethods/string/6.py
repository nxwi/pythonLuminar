# count the total number of digits and alphabets in an alphanumeric string inout by the user

x = input('Enter the string:')

a = 0
d = 0

for i in x:
    if i.isalpha():
        a += 1
    elif i.isnumeric():
        d += 1
print("No. of alphabets:", a)
print("No. of digits:", d)
