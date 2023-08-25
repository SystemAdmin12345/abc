'''
This contains the loop.
'''

import time

def wait(number):
    '''
    Shortens the waiting function
    '''
    time.sleep(number)


'''

'''
MODE = 0
NUMBER = 0
CYCLE = 0

print(NUMBER)
while CYCLE < 10:
    if MODE == 0:
        while NUMBER < 10:
            NUMBER += 1
            if NUMBER == 10:
                break
            print(NUMBER)
            wait(0.25)
        print(NUMBER)
        MODE = 1
        CYCLE += 1
    wait(0.25)
    if MODE == 1:
        while NUMBER > 0:
            NUMBER -= 1
            print(NUMBER)
            wait(0.25)
        MODE = 0
        CYCLE += 1
    wait(0.25)
    