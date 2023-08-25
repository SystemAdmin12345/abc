"""
A calculator for the fibonacci sequence (not 100% accurate)
"""

print("Welcome to Fibonacci Sequence Calculator!")
print("Disclaimer: This program is limited and not ")

DATA_1 = 0  # The main number, gets printed.
DATA_2 = 1  # The secondary number.
BUFFER = 0  # A temporary buffer to store data before overriding variables.
CYCLES = 0  # Amount of steps.
MAX_CYCLES = 5  # Default Variable.


try:
    MAX_CYCLES = int(input("How many numbers do you want? "))
except ValueError:
    print("You put in a non-integer!")
print(f"Outputting {MAX_CYCLES} number(s).")



while CYCLES < MAX_CYCLES:
    print(DATA_1)
    BUFFER = DATA_1 + DATA_2
    DATA_1 = DATA_2
    DATA_2 = BUFFER
    BUFFER = 0
    CYCLES += 1
