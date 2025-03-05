import copy

l1 = [1, [2, 3]]
l2 = copy.deepcopy(l1)
print(f"id(l1[1]): {id(l1)}\tid(l2[1]): {id(l2)}")
print(f"l1: {l1}\t\tl2: {l2}")
l1[1][0] = 20
print(f"l1: {l1}\tl2: {l2}")
"""
l1 = [1, [2, 3]]
l2 = copy.copy(l1)
print(f"id(l1): {id(l1)}\tid(l2): {id(l2)}")
print(f"l1: {l1}\t\tl2: {l2}")
l1[1][0] = 20
print(f"l1: {l1}\tl2: {l2}")"""

"""
l1 = [1, 2, 3]
l2 = copy.copy(l1)
print(f"id(l1): {id(l1)}\tid(l2): {id(l2)}")
print(f"l1: {l1}\tl2: {l2}")
l1[0] = 10
print(f"l1: {l1}\tl2: {l2}")"""



"""
d1 = 5
d2 = d1
print(f"d1: {d1}\td2: {d2}")
d1 = 10
print(f"d1: {d1}\td2: {d2}")

l1 = [1, 2, 3]
l2 = l1
print(f"l1: {l1}\tl2: {l2}")
l1[0] = 10
print(f"l1: {l1}\tl2: {l2}")"""