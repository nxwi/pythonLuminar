# Write a program that calculates the power of a number (a^b)

base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

power = 1
for i in range(exponent):
    power *= base

print(base, "raised to the power of", exponent, "is", power)
