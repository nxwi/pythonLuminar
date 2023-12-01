# Create a program that converts a decimal number to binary.

n = int(input("Enter a decimal number: "))

binary = ""
while n > 0:
    binary = str(n % 2) + binary
    n //= 2

print("Binary representation:", binary)
