# Create a program to find and print the Fibonacci sequence up to N terms.

n = int(input("Enter the number of terms: "))
x = 0
y = 1
for i in range(n):
    if i == 0:
        print(x)
    elif i == 1:
        print(y)
    else:
        z = x + y
        x = y
        y = z
        print(y)
