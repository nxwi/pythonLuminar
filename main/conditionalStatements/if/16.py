# Program to find the largest of 3 number

x = int(input("Enter the value of x:"))
y = int(input("Enter the value of y:"))
z = int(input("Enter the value of z:"))

if x > y & x > z:
    print(x, "is the largest")
elif y > z:
    print(y, "is the largest")
else:
    print(z, "is the largest")
