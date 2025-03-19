def letter_count(s):
    """ build a dictionary with all the letters and initialize them
        to 0 in the beginning"""
    result_key = set(s)
    result = dict.fromkeys(result_key, 0)
    for letter in s:
        result[letter] = result[letter] + 1
    return result


    """ set a default value if the key is not in the dictionary"""
    """
    result = {}
    for letter in s:
        result[letter] = result.get(letter, 0) + 1
    return result"""

    """ Basic solution"""
    """
    result = {}
    for letter in s:
        if letter in result:
            #result[letter] = result[letter] + 1
            result[letter] = result.get(letter) + 1
        else:
            #result[letter] = 1
            result.update({letter: 1})
    return result"""


def main():
    s = "w3resource"
    count = letter_count(s)
    print(count)

if __name__ == "__main__":
    main()