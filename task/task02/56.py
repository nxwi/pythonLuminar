# Create a program that generates a random password of a given length.

import random

length = int(input("Enter the length of the password: "))

password = ""
for _ in range(length):
    char_type = random.randint(1, 4)
    if char_type == 1:
        password += chr(random.randint(65, 90))  # uppercase letter
    elif char_type == 2:
        password += chr(random.randint(97, 122))  # lowercase letter
    elif char_type == 3:
        password += chr(random.randint(48, 57))  # digit
    else:
        password += chr(random.randint(33, 47))  # symbol

print("Generated password:", password)
