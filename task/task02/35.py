# Write a Python program to find the LCM (The Least Common Multiple) of two numbers.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

greater = num1 if num1 > num2 else num2
while True:
    if greater % num1 == 0 and greater % num2 == 0:
        lcm = greater
        break
    greater += 1

print("The LCM of", num1, "and", num2, "is", lcm)
