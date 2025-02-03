l = [5, 4, 7, 2, 9, 8]

""" create a new list k
    (the elements in k is the
    elements in l add 1 )
    then print k """

# k = l <- not workable
"""
k = []
for e in l:
    k.append(e + 1) """

k = [(e + 1) for e in l]

print(l) # [5, 4, 7, 2, 9, 8]
print(k) # [6, 5, 8, 3, 10, 9]
