````

MAX_CYCLES = 5 # Default Variable
DATA_1 = 0
DATA_2 = 1
BUFFER = 0
CYCLES = 0
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
