morseCode = { 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
              'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
              'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..'}

original = "Pyt hon"

# convert all characters to uppercase ==> str.upper()
originalUpper = original.upper()

# conver each letter in original to morse code
morseList = []
for letter in originalUpper:
    if letter in morseCode:
        morseList.append(morseCode[letter])
    else:
        morseList.append("/")
    """
    if letter.isalpha():
        print(morseCode[letter])
    else:
        print("/")
    """
    """
    if letter == " ":
        print("/")
    else:
        print(morseCode[letter])"
    """
#print(morseList)
# merge all the morse code into a single string
solution = " ".join(morseList)
print(solution)
# ".--. -.-- - / .... --- -."