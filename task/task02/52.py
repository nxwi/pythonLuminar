# Create a program to count the number of uppercase and lowercase letters in a string.

text = input("Enter a string: ")

uppercase, lowercase = 0, 0
for char in text:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1

print("Number of uppercase letters:", uppercase)
print("Number of lowercase letters:", lowercase)
