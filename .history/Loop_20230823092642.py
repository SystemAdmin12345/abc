import time

def wait(number)
    


MODE = 0
NUMBER = 0
CYCLE = 0

while CYCLE < 10:
    if MODE == 0 :
        while NUMBER < 10:
            print(NUMBER)
            NUMBER = NUMBER + 1
        print(NUMBER)
        MODE = 1
        CYCLE = CYCLE + 1
    if MODE == 1:
        while NUMBER > 0:
            NUMBER = NUMBER - 1
            print(NUMBER)
        MODE = 0
        CYCLE = CYCLE + 1
