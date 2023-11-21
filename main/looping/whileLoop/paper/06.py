# Program to find the product of numbers between the range 1 to 100 except the multiple of 7 and 13

x = 1
y = 1

while x <= 100:
    if (x % 7 != 0) or (x % 13 != 0):
        y *= x
    x += 1
print(y)
