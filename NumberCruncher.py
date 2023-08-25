
import time
number = 0
countdown = 5
print("Numbers 0 to 15,000,000")
time.sleep(5)
while countdown > 0:
    print(countdown)
    time.sleep(1)
    countdown = countdown - 1
print("Starting")
time.sleep(1)
while number < 15000000:
    print(number)
    number = number + 1
print("15,000,000 Yay!")
