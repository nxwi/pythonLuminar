# Greatest of three numbers

greatest = lambda a, b, c: a if (a > b and a > c) else (b if b > c else c)

print(greatest(1, 2, 3))
