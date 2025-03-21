import pprint
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}


k1 = set(d1.keys())
k2 = set(d2.keys())
kall = k1 | k2

dic_sum3 = {e: d1.get(e, 0) + d2.get(e, 0) for e in kall}
print(dic_sum3)
pprint.pprint(dic_sum3)

"""
dic_sum2 = dict.fromkeys(kall, 0)
for e in dic_sum2:
    dic_sum2[e] = d1.get(e, 0) + d2.get(e, 0)
print(dic_sum2)
"""

"""
dic_sum1 = dict.fromkeys(kall, 0)
for (k, v) in d1.items():
    dic_sum1[k] = dic_sum1[k] + v
for (k, v) in d2.items():
    dic_sum1[k] = dic_sum1[k] + v
print(dic_sum1)
"""

"""
for e in d2:
    if e in d1:
        d1[e] = d1[e] + d2[e]
    else:
        d1[e] = d2[e]

print(d1)
"""


"""
for e in d1:
    print(e)

print(d1.keys())
print(d1.values())
print(d1.items())
"""

