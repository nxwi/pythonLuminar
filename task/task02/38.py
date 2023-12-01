# Create a program to calculate the sum of all natural numbers up to a given N

n = int(input("Enter the number: "))

sum0 = 0
for i in range(1, n + 1):
    sum0 += i

print("The sum of all natural numbers up to", n, "is", sum0)
