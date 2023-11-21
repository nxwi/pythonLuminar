# write a program to count total no. of vowels in a string input by the user

x = input('Enter the string:').lower()

n = 0

for i in x:
    if i in 'aeiou':
        n += 1
print(n)
