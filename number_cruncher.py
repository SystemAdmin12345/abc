"""
This script crunches numbers!
"""

import time
NUMBER = 0
COUNTDOWN = 5
print("Numbers 0 to 15,000,000")
time.sleep(5)
while COUNTDOWN > 0:
    print(COUNTDOWN)
    time.sleep(1)
    COUNTDOWN = COUNTDOWN - 1
print("Starting")
time.sleep(1)
while NUMBER < 15000000:
    print(NUMBER)
    NUMBER = NUMBER + 1
print("15,000,000 Yay!")
