# 1. What is the difference between '==' and 'is' in Python?

"""
'==' checks whether their value is equal
'is' checks whether they refer to the same memory location
"""

# 2. what is the difference between compiler and interpreter language?

"""
Compiler: A compiler translates the entire source code of a program
Interpreter: An interpreter processes the source code line by line
"""

# 3. Explain the syntax of the 'if' ,'else' and 'elif' statements in Python.

"""
if Statement:-
if condition:
    # Code to execute if the condition is true

else Statement:-
if condition:
    # Code to execute if the condition is true
else:
    # Code to execute if the condition is false

elif Statement:-
if condition1:
    # Code to execute if condition1 is true
elif condition2:
    # Code to execute if condition2 is true
else:
    # Code to execute if neither condition1 nor condition2 is true
"""

# 4. Write a Python program to determine whether a given year is a leap year or not. Leap years are divisible by 4,
#    but not divisible by 100, it must also be divisible by 400 to be a leap year.?

"""
year = int(input("Enter the year:"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
"""

# 5. Write a Python program that calculates the discount for a purchase based on the total cost:
#    • If the total cost is $100 or more, apply a 10% discount.
#    • If the total cost is between $50 and $99, apply a 5% discount.
#    • If the total cost is less than $50, apply no discount.

"""
cost = int(input("Total cost:"))

if cost >= 100:
    print("Discount:", cost * 0.1, "\nFinal cost:", cost - (cost * 0.1))
elif cost >= 50:
    print("Discount:", cost * 0.05, "\nFinal cost:", cost - (cost * 0.05))
else:
    print("Discount: 0 \nFinal cost:", cost)
"""

# 6. Create a Python program that prints the Fibonacci sequence up to a specified number of terms using a for loop?

"""
n = int(input("Enter the number terms:"))

a = 0
b = 1

print(a, end=' ')

for i in range(1, n):
    print(b, end=' ')
    c = a + b
    a = b
    b = c
"""

# 7. Check a number is Armstrong or not using for loop?

"""
arm = 0
n = int(input("Enter a number:"))
t = n
l = len(str(n))
for i in range(l):
    a = n%10
    arm += a**l
    n //= 10
if arm == t:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")
"""

# 8. Print a right angle star pattern according to the user input?

"""
n = int(input("Enter the number of row:"))

for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()
"""

# 9. Find factors of a number input by the user using for loop?

"""
n = int(input("Enter the number:"))

for i in range(1,n+1):
    if n % i == 0:
        print(i, end=" ")
"""

# 10. What is the latest version of python?

"""
v3.12
"""
