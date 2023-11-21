# Print the pattern
# a
# b b
# c c c

n = ord('a')

for i in range(n, n+3):
    for j in range(n, i+1):
        print(chr(i), end=' ')
    print()
