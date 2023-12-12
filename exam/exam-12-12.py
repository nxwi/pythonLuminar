# 1. Create a function to pass value into it and print a pyramid pattern?
"""
def pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1 - i):
            print(' ', end='')
        for j in range(1, i + 1):
            print('*', end=' ')
        print()


pyramid(5)
"""

# 2. [5,2,3,1,4] find the largest element in the given list ?
'''
data = [5, 2, 3, 1, 4]
largest = data[0]
for element in data:
    if element > largest:
        largest = element
print(f"Largest element: {largest}")
'''

# 3. {'b':2, 'c':3, 'a':1} sort the dict?
'''
data = {'b': 2, 'c': 3, 'a': 1}
x = dict(sorted(data.items()))
print(f"Sorted dictionary: {x}")
'''

# 4. What is symmetric_difference _update and intersection _update ?
'''
symmetric_difference_update: Returns a set with the elements that are in the other set but not in itself, and removes 
                             elements that are in both sets.
intersection_update: Returns a set with the elements that are in both sets and itself.
'''

# 5. Input a string, remove duplicates and finally print the reverse of the string?
'''
string0 = input("Input:")
string1 = ''.join(set(string0))
print(f"Reversed string after removing duplicates: {string1}")
'''

# 6. Explain types of arguments with example?
'''
Required Arguments: These arguments must be provided when calling the function.
    Example: def greet(name):
                 print(f"Hello, {name}!")
             greet("John")

Keyword Arguments: These arguments are named and can be provided in any order when calling the function.
    Example: def greet_with_age(name, age):
                 print(f"Hi {name}, you look great for your {age}!")
             greet_with_age(age=25, name="Jane")

Default Arguments: These arguments have pre-defined values if not explicitly provided.
    Example: def greet_friend(name="Friend"):
                 print(f"Hey there {name}!")
             greet_friend("John")

             
Variable-Length Arguments: These arguments can take an arbitrary number of values using *args or **kwargs.
    Example: def print_all(*args, **kwargs):
                 print("Positional:", args)
                 print("Keyword:", kwargs)
             print_all(1, 2, 3, name="John", age=30)

'''

# 7. Using random module select choices, integers and float values ?
'''
import random

choices = ["apple", "banana", "cherry"]
randomChoice = random.choice(choices)
print(f"Random choice: {randomChoice}")

randomInteger = random.randint(1, 10)
print(f"Random integer: {randomInteger}")

randomFloat = random.uniform(1.0, 5.0)
print(f"Random float: {randomFloat}")
'''

# 8. How do you remove a file in python ?
'''
import os

os.remove("filename.txt")
'''

# 9. How to delete a directory that contains files in python ?
'''
import os

os.removedirs("directory_name")
'''

# 10. Write a python program to create a class representing a shopping cart
#     Include methods for adding removing , view , and calculating the total price?
'''
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.prices = {}

    def addItem(self, item, price):
        self.items.append(item)
        self.prices[item] = price

    def removeItem(self, item):
        if item in self.items:
            self.items.remove(item)
            del self.prices[item]

    def viewItems(self):
        print("Items in cart:")
        for item in self.items:
            print(f"- {item}")

    def getTotalPrice(self):
        totalPrice = 0
        for item, price in self.prices.items():
            totalPrice += price
        return totalPrice


cart = ShoppingCart()
cart.addItem("book", 10)
cart.addItem("pen", 2)
cart.viewItems()
cart.addItem("tv", 500)
cart.viewItems()
cart.removeItem("book")
cart.viewItems()
print(f"Total price: {cart.getTotalPrice()}")
'''

# 11. Write a python program to create a class representing a circle include methods to calculate area and perimeter
'''
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius ** 2

    def getPerimeter(self):
        return 2 * math.pi * self.radius


circle = Circle(5)
print(f"Area: {circle.getArea()}")
print(f"Perimeter: {circle.getPerimeter()}")
'''

# 12. write a python program that executes an operation on a list and handles an indexError if the index is out of
# range?
'''
data = [1, 2, 3]

try:
    element = data[5]
    print(f"Element at index 5: {element}")
except IndexError:
    print("Index out of range! Please provide a valid index.")
'''

# 13. write a python program to match a string that contains only uppercase , lowercase, numbers , and underscore?
'''
import re

pattern = r"^[a-zA-Z0-9_]+$"

string1 = "This_is_valid"
string2 = "123abc"
string3 = "special@symbol"

if re.match(pattern, string1):
    print(f"'{string1}' matches the pattern")
else:
    print(f"'{string1}' does not match the pattern")

if re.match(pattern, string2):
    print(f"'{string2}' matches the pattern")
else:
    print(f"'{string2}' does not match the pattern")

if re.match(pattern, string3):
    print(f"'{string3}' matches the pattern")
else:
    print(f"'{string3}' does not match the pattern")
'''
# 14. What is the difference between mutable and immutable data types ?
#     List out mutable data types and immutable datatypes?
'''
Mutable data types: These can be modified after they are created.
    Examples: lists, dictionaries, sets.
Immutable data types: These cannot be modified after they are created.
    Examples: strings, tuples, integers, floats.
'''

# 15. Using lambda function solve the largest of 3 numbers ?
'''
largest = lambda x, y, z: max(x, y, z)

numbers = [5, 10, 22]
largest_number = largest(*numbers)

print(f"Largest number in the list: {largest_number}")
'''
