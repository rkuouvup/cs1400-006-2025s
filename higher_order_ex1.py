toys = ("bicycle", "train", "doll", "teddy bear",
        "kite", "ball", "video game set")

sorted_toys = sorted(toys, key=len)
print(f"Sorted list based on the string length: {sorted_toys}")

def secondLetter(s):
    return s[1]

secondLetter_toys = sorted(toys, key=secondLetter)
print(f"Sorted list based on the second letter: {secondLetter_toys}")

def lastLetter(s):
    return s[-1]

lastLetter_toys = sorted(toys, key=lastLetter)
print(f"Sorted list based on the second letter: {lastLetter_toys}")