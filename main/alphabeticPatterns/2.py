# Print the pattern
# c c c
# b b
# a

n = ord('a')

for i in range(n+3, n, -1):
    for k in range(n, i):
        print(chr(i-1), end=" ")
    print()
