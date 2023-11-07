import random

# li = [1, 2, 3, 4]
# print(random.choice(li))
print(random.choice([1, 2, 3, 4]))

# st = 'abcd'
# print(random.choice(st))
print(random.choice('abcd'))

print(random.randint(100, 200))  # inclusive of both endpoints
print(random.randrange(1, 10))  # exclusive of the endpoint

print(random.uniform(10, 2))

li = [1, 2, 3, 4]
print(random.shuffle(li))
print(li)
