
import time

def wait(number):
    time.sleep(number)


MODE = 0
NUMBER = 0
CYCLE = 0

print(NUMBER)
while CYCLE < 10:
    if MODE == 0 :
        while NUMBER < 10:
            NUMBER = NUMBER + 1
            print(NUMBER)
            wait(0.5)
        print(NUMBER)
        MODE = 1
        CYCLE = CYCLE + 1
    if MODE == 1:
        while NUMBER > 0:
            NUMBER = NUMBER - 1
            print(NUMBER)
            wait(0.5)
        MODE = 0
        CYCLE = CYCLE + 1
    wait(0.25)
