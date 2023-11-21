# Write a Python program to find the second-largest element in a list.

numbers = input("Enter the list of numbers: ").split()

for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        if int(numbers[i]) > int(numbers[j]):
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp

second_largest = int(numbers[-2])

print("The second largest element in the list is:", second_largest)
