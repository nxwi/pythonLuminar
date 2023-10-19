# Program to count the number of alphabets and digits in the given list

li = [1, 2, 3, 'a', 'b', 'c', 'd']

a = 0
d = 0

for i in li:
    if str(i).isalpha():
        a += 1
    elif str(i).isnumeric():
        d += 1

print('Alpha=', a)
print('Digits=', d)
