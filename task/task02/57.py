# Write a program to find and print the factors of a number.

n = int(input("Enter a number: "))

print("Factors of", n, ":")
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
