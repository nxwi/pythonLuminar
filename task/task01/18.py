# Create a program to count the number of vowels in a string.

x = input("Enter the string: ")

count = 0
for i in x:
    if i in "AEIOUaeiou":
        count += 1

print("The number of vowels in the string is:", count)
