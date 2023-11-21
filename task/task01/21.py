# Write a program that generates a random number and asks the user to guess it.

import random

random_number = random.randint(1, 10)
user_guess = int(input("Enter your guess between 1 and 10: "))
while user_guess != random_number:
    if user_guess < random_number:
        print("Your guess is too low. Try again.")
    else:
        print("Your guess is too high. Try again.")
    user_guess = int(input("Enter your guess: "))
print("Congratulations! You guessed the correct number:", random_number)
