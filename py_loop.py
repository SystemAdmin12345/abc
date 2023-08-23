"""
This script contains a basic loop.
"""


import time


# Adjustable Variables

DELAY = 0.25  # 0.25 by default
MIN = 0  # Default: 0
MAX = 10  # Default: 10
MAX_CYCLES = 5  # Default: 5
INCREMENT = 1  # Default: 1


def wait(number):
    """
    Shortens the waiting function
    """
    time.sleep(number)


# Initialize Variables
MODE = 0
NUMBER = MIN
CYCLE = 0

print(NUMBER)
while CYCLE < MAX_CYCLES:
    if MODE == 0:
        while NUMBER < MAX:
            NUMBER += INCREMENT
            if NUMBER == MAX:
                break
            print(NUMBER)
            wait(DELAY)
        print(NUMBER)
        MODE = 1
        CYCLE += 1
    wait(DELAY)
    if MODE == 1:
        while NUMBER > MIN:
            NUMBER -= INCREMENT
            print(NUMBER)
            wait(DELAY)
        MODE = 0
        CYCLE += 1
    wait(DELAY)
