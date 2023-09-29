# Program to find the sum of first 10 odd numbers

x = 0

for i in range(1, 21):
    if i % 2 == 1:
        x += i
print(x)
