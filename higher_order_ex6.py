l = [6, 3, 4, 8, 1]

"""
Define a function to find the maximum element
"""
def findMax_for(lst):
    result = lst[0]
    for e in lst[1:]:
        if e > result:
            result = e
    return result

print(f"The maximum number is {findMax_for(l)}")


def myMax(a, b):
    if a >= b:
        return a
    else:
        return b

def find_Max_rec1(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return myMax(lst[0], find_Max_rec1(lst[1:]))


print(f"The maximum number is {find_Max_rec1(l)}")

import math

def find_Max_rec2(lst):
    if lst == []:
        return -math.inf
    else:
        return myMax(lst[0], find_Max_rec2(lst[1:]))

print(f"The maximum number is {find_Max_rec2(l)}")

import functools
print(functools.reduce(myMax, l, -math.inf))
print(functools.reduce(lambda a, b: a if a >= b else b, l, -math.inf))