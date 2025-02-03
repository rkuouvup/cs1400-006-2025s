import random
l = [6, -2, 3, 8, -5, -1]
#   [True, False, True, True, False, False]

"""
k = []
for e in l:
    if e > 0:
        k.append(True)
    else:
        k.append(False) """

k = [random.randint(500, 1000) if e > 0 else random.randint(0, 10) for e in l]

print(k)