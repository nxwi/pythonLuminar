# Write a Python program to find the minimum and maximum elements in a list.

numbers = [int(x) for x in input("Enter a list of numbers: ").split()]

min_val = min(numbers)
max_val = max(numbers)

print("Minimum:", min_val)
print("Maximum:", max_val)
