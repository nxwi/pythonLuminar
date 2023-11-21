# Program to check a number is positive negative or zero

n = int(input("Enter the number: "))

check = lambda x: 'zero' if x == 0 else ('+ve' if x > 0 else '-ve')

print(check(n))
