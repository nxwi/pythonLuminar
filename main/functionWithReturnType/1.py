# Program to find a number is odd or even using return type

def odd(n):
    if n % 2 == 1:
        return '%d is odd' % n
    else:
        return '%d is even' % n


print(odd(1))
print(odd(2))
