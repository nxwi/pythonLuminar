# Create a program to calculate the sum of all prime numbers from 1 to 100.

primes = []
for number in range(2, 101):
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(number)

total_sum = sum(primes)
print("The sum of all prime numbers from 1 to 100 is:", total_sum)
