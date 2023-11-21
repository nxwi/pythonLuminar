# Create a function using def and pass a list of alphabets as an argument and using lambda filter out vowels
# and return the list vowels

def vowels(li):
    return list(filter(lambda i: i in 'aeiouAEIOU', li))


li1 = input("Enter:").split()

li2 = []

for i in li1:
    li2.append(i)

print(vowels(li2))
