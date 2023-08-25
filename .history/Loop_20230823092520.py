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
    elsif MODE == 1:
        while NUMBER > 0:
            NUMBER = NUMBER - 1
            print(NUMBER)
        
