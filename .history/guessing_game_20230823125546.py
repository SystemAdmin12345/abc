"""
Number Guessing Game
"""

import random  # Imports "random" for the RNG part to work.

# Adjustable Values
ATTEMPTS = 3  # How many attempts the player gets (Default: 3).
MAX_NUMBER = 10  # Default: 10
MIN_NUMBER = 1  # Default: 1

# Core

while ATTEMPTS > 0:
    print("====================")
    DISPLAY = f'
What number am I thinking of? ({MIN_NUMBER}-{MAX_NUMBER})\nYou have {ATTEMPTS} attempt(s).\nYour Answer: '
    NUMBER = random.randint(MIN_NUMBER, MAX_NUMBER)  # RNG Number
    try:
        USER_NUMBER = int(input(DISPLAY))
    except ValueError:
        print("You put something that is not an integer.")
        continue

    if USER_NUMBER < MIN_NUMBER or USER_NUMBER > MAX_NUMBER:
        print(
            "You put a number that's outside of the range. Please guess between",
            MIN_NUMBER,
            "and",
            MAX_NUMBER,
        )
        continue

    if NUMBER == USER_NUMBER:
        print(
            f"Congratulations! You guessed the correct number with {ATTEMPTS} attempt(s) remaining."
        )
        break

    if NUMBER != USER_NUMBER:
        ATTEMPTS -= 1
        print("Sike! That's the wrong number!\nAttempt(s) Left:", ATTEMPTS)

if ATTEMPTS != 0:
    print("You won the game!")

if ATTEMPTS == 0:
    print("You lost the guessing game!")
