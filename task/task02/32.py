# Create a program that checks if a given number is a perfect square.

import math

number = int(input("Enter a number: "))
square_root = math.sqrt(number)
if number % square_root == 0:
    print(number, "is a perfect square")
else:
    print(number, "is not a perfect square")
