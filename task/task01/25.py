# Write a program to find the common elements between two lists.

list1 = input("Enter the first list: ").split()
list2 = input("Enter the second list: ").split()

common_elements = set(list1) & set(list2)

print("The common elements between the two lists are:", common_elements)
