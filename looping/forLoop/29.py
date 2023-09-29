# take initial and final value from use and even numbers between the range including the range

x = int(input("Enter the start:"))
y = int(input("Enter the end:"))

for i in range(x, y + 1):
    if i % 2 == 0:
        print(i)
