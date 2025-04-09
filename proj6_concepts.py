"""
sep_args = list(range(3, 6))
print(sep_args)

arg = [3, 6]
print(list(range(arg[0], arg[1])))
single_arg = list(range(*arg))
print(single_arg)
"""

l1 = [11, 12, 13, 14, 15]
l2 = [21, 22, 23, 24, 25]
l3 = [31, 32, 33, 34, 35]
l4 = [41, 42, 43, 44, 45]

zip12 = tuple(zip(l1, l2))
print(zip12)
zip123 = tuple(zip(l1, l2, l3))
print(zip123)

k = [1, 2, 3]
k1, k2, k3 = k
print(f"{k1}, {k2}, {k3}")

myData1 = ((1, "a"), (2, "b"), (3, "c"), (4, "d"))
print(list(zip(*myData1)))

para1, para2 = zip(*myData1)
print(f"para1: {para1}, para2: {para2}")