"""
Hello
"""

INPUT = "No"
DONE = 0

print("\nWelcome to Skip Code Checker!")
print("Enter your Skip Code!\n")

while DONE == 0:
    INPUT = input("Skip Code: ")

    if INPUT == "gay":
        DONE = 1
        print("\nSo you said gay, huh? Skip Code Accepted, giving Gay Badge.....")
        print("You got a badge! \nBadge: Gay")
    if INPUT == "Among us":
        DONE = 1
        print("AMOGUS!")
    if INPUT == "Kaching":
        print("Giving money...")
        print("Didn't work...\n")
    else:
        print(f"You put the wrong code! ({INPUT})")
print("\n")
