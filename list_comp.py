l = [6, -2, 3, 8, -5, -1]

"""
k = []
for e in l:
    if e > 0:
        k.append(e)   """

k = [e for e in l if e > 0]

print(k)