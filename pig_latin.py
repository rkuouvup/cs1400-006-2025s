def pigLatin(w):
    vowels = "aeiou"
    if w.startswith(tuple(vowels)):
        return w + "way"
    else:
        vowelIndex = 0
        for i in range(1, len(w)):
            if w[i] in vowels:
                vowelIndex = i
                break
        return w[vowelIndex:] + w[:vowelIndex] + "ay"

def main():
    lst = ["happy", "glove", "egg", "inbox", "pig", "latin", "banana", \
           "friends", "smile", "string", "eat", "omelet", "are"]
    result = (list(map(pigLatin, lst)))
    for (w1, w2) in zip(lst, result):
        print(f"{w1:10}{w2}")

if __name__ == "__main__":
    main()