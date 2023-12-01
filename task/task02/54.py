# Create a program to calculate the sum of a geometric series.

a = float(input("Enter the first term: "))
r = float(input("Enter the common ratio: "))
n = int(input("Enter the number of terms: "))

if r == 1:
    sum_value = a * n
else:
    sum_value = a * (1 - r ** n) / (1 - r)

print("Sum of the geometric series:", sum_value)
