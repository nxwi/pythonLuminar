# Create a program that sorts a list of numbers in ascending order.

numbers = input("Enter the list of numbers: ").split()

for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        if int(numbers[i]) > int(numbers[j]):
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp

print("The sorted list of numbers is:", numbers)
