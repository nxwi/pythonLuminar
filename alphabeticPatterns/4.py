# Print the pattern
# A
# B B
# C C C

n = ord('A')

for i in range(n, n+3):
    for j in range(n, i+1):
        print(chr(i), end=' ')
    print()
