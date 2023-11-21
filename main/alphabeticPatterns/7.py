# e
# d e
# c d e
# b c d e
# a b c d e
# E
# D E
# C D E
# B C D E
# A B C D E

for i in range(97, 102):
    for j in range(i+1, 97, -1):
        print(chr(199-j), end=' ')
    print()

for i in range(65, 70):
    for j in range(i+1, 65, -1):
        print(chr(135-j), end=' ')
    print()
