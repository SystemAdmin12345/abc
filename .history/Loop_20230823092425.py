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
    else if MODE == 1:
        