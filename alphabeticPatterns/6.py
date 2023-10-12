# Print the pattern
#     A
#   B B
# C C C

n = ord('A')

for i in range(n, n+3):
    for k in range(n+2-i):
        print(end='  ')
    for j in range(n, i+1):
        print(chr(i), end=' ')
    print()

for i in range(n+2, n, -1):
    for k in range(n+3-i):
        print(end='  ')
    for j in range(i-n):
        print(chr(i-1), end=' ')
    print()
