# Program to accept two numbers and mathematical operators and perform operation accordingly

x = int(input("Enter the first number:"))
y = int(input("Enter the second number:"))
z = input("Enter the operator:")

if z == "+":
    print(x + y)
elif z == "-":
    print(x - y)
elif z == "*":
    print(x * y)
elif z == "/":
    print(x / y)
else:
    print("Unknown operator")
