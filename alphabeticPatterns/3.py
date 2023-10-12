# Print the pattern
# a a a
# b b
# c

n = ord('a')

for i in range(n, n+3):
    for k in range(n+3-i):
        print(chr(i), end=" ")
    print()
