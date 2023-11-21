# Accept the age of 4 people and display the youngest one

a = int(input("Enter the age of 1st person:"))
b = int(input("Enter the age of 2nd person:"))
c = int(input("Enter the age of 3rd person:"))
d = int(input("Enter the age of 4th person:"))

if (a < b) & (a < c) & (a < d):
    print("1st person with", a, "age is the youngest")
elif (b < c) & (b < d):
    print("2nd person with", b, "age is the youngest")
elif c < d:
    print("3rd person with", c, "age is the youngest")
else:
    print("4th person with", d, "age is the youngest")
