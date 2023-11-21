# Program to display sum of both even and odd numbers that fall between 12 and 37

x = 0
y = 0

for i in range(12, 37):
    if i % 2 == 1:
        x += i
    elif i % 2 == 0:
        y += i
print("Sum of odd numbers=", x)
print("Sum of even numbers=", y)
