# Program to print multiplication table of a number input by the user

x = int(input("Enter the value:"))

for i in range(1, 11):
    print(x, "X", i, "=", x*i)
