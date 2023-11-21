# Largest of four numbers

compare = lambda x, y: x if x > y else y

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))

largest = compare(compare(a, b), compare(c, d))

print("The largest number is:", largest)
